from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import uuid
from datetime import datetime
import mysql.connector

app = Flask(__name__)
CORS(app)

# Configura la connessione al database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="192837465",
    database="event_management"
)

@app.route('/registration', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    print("il nome è", name, email, password)
    
    # Genera un ID univoco
    user_id = str(uuid.uuid4())

    # Ottieni la data e l'ora corrente
    created_at = datetime.now()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (id, name, email, password, created_at) VALUES (%s, %s, %s, %s, %s)",
                       (user_id, name, email, hashed_password, created_at))
        db.commit()
        cursor.close()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'message': 'Errore durante la registrazione'}), 500

    return jsonify({'message': 'Registrazione avvenuta con successo'}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
