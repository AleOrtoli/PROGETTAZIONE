import bcrypt
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import connect

app = Flask(__name__)
CORS(app)

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
            response = {'message': 'Login avvenuto con successo', 'user_id': user[0]}
            return jsonify(response), 200
        else:
            response = {'message': 'Credenziali errate'}
            return jsonify(response), 401
    else:
        response = {'message': 'Utente non trovato'}
        return jsonify(response), 401

if __name__ == '__main__':
    app.run(port=5002, debug=True)
