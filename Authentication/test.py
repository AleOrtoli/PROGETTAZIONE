import unittest
import requests

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:5002/authenticate'

    def test_authenticate_success(self):
        # Simula una richiesta di autenticazione corretta
        response = requests.post(self.base_url, json={'email': 'MarioMario@gmail.com', 'password': 'Mario'})
        data = response.json()
        
        # Verifica che il codice di stato della risposta sia 200
        self.assertEqual(response.status_code, 200)
        # Verifica che il messaggio di risposta sia corretto
        self.assertEqual(data['message'], 'Login avvenuto con successo')

    def test_authenticate_invalid_credentials(self):
        # Simula una richiesta di autenticazione con credenziali errate
        response = requests.post(self.base_url, json={'email': 'test@example.com', 'password': 'wrong_password'})
        data = response.json()
        
        # Verifica che il codice di stato della risposta sia 401
        self.assertEqual(response.status_code, 401)
        # Verifica che il messaggio di risposta sia corretto
        self.assertEqual(data['message'], 'Utente non trovato')

    def test_authenticate_user_not_found(self):
        # Simula una richiesta di autenticazione per un utente non trovato
        response = requests.post(self.base_url, json={'email': 'nonexistent@example.com', 'password': 'password'})
        data = response.json()
        
        # Verifica che il codice di stato della risposta sia 401
        self.assertEqual(response.status_code, 401)
        # Verifica che il messaggio di risposta sia corretto
        self.assertEqual(data['message'], 'Utente non trovato')

if __name__ == '__main__':
    unittest.main()
