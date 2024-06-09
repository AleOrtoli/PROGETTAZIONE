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
 
    response = requests.post(AUTH_SERVICE_URL, json={'email': email, 'password': password})
    auth_status_code = response.status_code
    auth_response = response.json()
 
    if auth_status_code == 200:
        return jsonify(auth_response), 200
    else:
        return jsonify(auth_response), auth_status_code
 
if __name__ == '__main__':
    app.run(port=5000, debug=True)