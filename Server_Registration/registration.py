from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import uuid
from datetime import datetime
import mysql.connector
import re

app = Flask(__name__)
CORS(app)

# Configura la connessione al database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="192837465",
    database="event_management"
)

def validate_password(password):
    # Controlla che la password sia lunga almeno 8 caratteri
    if len(password) < 8:
        return False
    # Controlla che la password contenga almeno una maiuscola
    if not any(char.isupper() for char in password):
        return False
    # Controlla che la password contenga almeno un carattere speciale
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

@app.route('/registration', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    cell = data.get('phone')
    password = data.get('password')

    print("DATI: ", name, email, cell, password)

    # Verifica che l'email contenga la chiocciola
    if not email or '@' not in email:
        return jsonify({'error': 'Email non valida. Deve contenere una chiocciola.'}), 400
    
    # Verifica che il numero di cellulare sia valido
    if not cell or len(cell) != 10 or not cell.isdigit():
        return jsonify({'error': 'Numero di cellulare non valido. Deve essere composto da 10 cifre numeriche.'}), 400
    
    # Verifica che la password soddisfi i criteri di sicurezza
    if not validate_password(password):
        return jsonify({'error': 'Password non valida. Deve essere lunga almeno 8 caratteri, contenere almeno una lettera maiuscola e un carattere speciale.'}), 400

    # Genera un ID univoco
    user_id = str(uuid.uuid4())

    # Ottieni la data e l'ora corrente
    created_at = datetime.now()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (id, name, email, password, created_at, cellulare) VALUES (%s, %s, %s, %s, %s, %s)",
                       (user_id, name, email, hashed_password, created_at, cell))
        db.commit()
        cursor.close()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        if err.errno == 1062:  # Duplicate entry error code
            return jsonify({'message': 'Email già esistente', 'error': str(err)}), 409
        return jsonify({'message': 'Errore durante la registrazione', 'error': str(err)}), 500

    return jsonify({'message': 'Registrazione avvenuta con successo'}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
