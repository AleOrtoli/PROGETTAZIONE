import bcrypt
import jwt
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Chiave segreta per la codifica dei token JWT
SECRET_KEY = 'il_tuo_segreto_super_segretissimo'

# Configura la connessione al database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="192837465",
    database="event_management"
)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        password_hash = user[3]
        if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
            # Creazione del token JWT
            token = jwt.encode({
                'user_id': user[0],
                'role': user[6],  # Supponendo che il ruolo dell'utente sia nella quinta colonna
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, SECRET_KEY, algorithm='HS256')

            response = {
                'message': 'Login avvenuto con successo',
                'token': token
            }
            return jsonify(response), 200
        else:
            response = {'message': 'Credenziali errate'}
            return jsonify(response), 401
    else:
        response = {'message': 'Utente non trovato'}
        return jsonify(response), 401

if __name__ == '__main__':
    app.run(port=5002, debug=True)
