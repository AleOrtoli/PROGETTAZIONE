from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
 
app = Flask(__name__)
CORS(app)
 
AUTH_SERVICE_URL = "http://localhost:5002/authenticate"
 
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    try:
        # Verifica che l'email contenga la chiocciola
        if not email or '@' not in email:
            return jsonify({'error': 'Email non valida. Deve contenere una chiocciola.'}), 400
        
        # verifica che email e password siano presenti nei dati
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Email e password sono obbligatori.'}), 400
   
        response = requests.post(AUTH_SERVICE_URL, json={'email': email, 'password': password})
        auth_status_code = response.status_code
        auth_response = response.json()
   
        if auth_status_code == 200:
            return jsonify(auth_response), 200
        else:
            return jsonify(auth_response), auth_status_code
    except requests.exceptions.RequestException as e:
        # Gestione delle eccezioni durante la richiesta al servizio di autenticazione
        return jsonify({'error': 'Errore di comunicazione con il servizio di autenticazione.', 'details': str(e)}), 500
if __name__ == '__main__':
    app.run(port=5000, debug=True)