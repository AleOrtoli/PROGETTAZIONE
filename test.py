import unittest
import requests
 
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000/login'
 
    def test_login_success(self):
        # Simula una richiesta di accesso con credenziali corrette
        response = requests.post(self.base_url, json={'email': 'MarioMario@gmail.com', 'password': 'Mario'})
        # Verifica che la risposta sia corretta
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Login avvenuto con successo')
 
    def test_login_failure(self):
        # Simula una richiesta di accesso con credenziali errate
        response = requests.post(self.base_url, json={'email': 'email@example.com', 'password': 'wrongpassword'})
        # Verifica che la risposta sia corretta
        self.assertEqual(response.status_code, 401)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Utente non trovato')

    def test_login_emailNonValida(self):
        # Simula una richiesta di accesso con credenziali errate
        response = requests.post(self.base_url, json={'email': 'emailexample.com', 'password': 'wrongpassword'})
        # Verifica che la risposta sia corretta
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Email non valida. Deve contenere una chiocciola.')
 
if __name__ == '__main__':
    unittest.main()