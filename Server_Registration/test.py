import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from registration import app
import mysql.connector
import requests

class RegistrationTestCase(unittest.TestCase):
    
    def setUp(self):
        # Configura l'applicazione Flask per il test
        self.base_url = 'http://localhost:5001/registration'
        self.app = app.test_client()
        self.app.testing = True

    def test_register_success(self):
        # Simula una registrazione con successo
        with patch('registration.mysql.connector.connect') as mock_connect:
            # Mock del cursore e della connessione del database
            mock_db = MagicMock(spec=mysql.connector.connection.MySQLConnection)
            mock_cursor = MagicMock(spec=mysql.connector.cursor.MySQLCursor)
            mock_connect.return_value = mock_db
            mock_db.cursor.return_value = mock_cursor

            # Mock della query di inserimento senza effettuare il commit
            mock_cursor.execute.return_value = None

            # Dati di esempio per la registrazione
            data = {
                'name': 'Matteo',
                'email': 'unique_matteo5@gmail.com',  # Utilizza un'email unica per il test
                'password': 'password123'
            }

            # Chiamata POST al nostro endpoint di registrazione
            response = self.app.post(self.base_url, json=data)
            
            # Verifica che la risposta sia 200 OK
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Registrazione avvenuta con successo', response.data)

            

    def test_register_duplicate_email(self):
        # Simula un'email duplicata durante la registrazione
        with patch('registration.mysql.connector.connect') as mock_connect:
            # Mock del cursore e della connessione del database
            mock_db = MagicMock(spec=mysql.connector.connection.MySQLConnection)
            mock_cursor = MagicMock(spec=mysql.connector.cursor.MySQLCursor)
            mock_connect.return_value = mock_db
            mock_db.cursor.return_value = mock_cursor

            # Simula un'eccezione del database per errore di duplicato
            mock_cursor.execute.side_effect = mysql.connector.IntegrityError(
                msg="Duplicate entry 'MarioMario@gmail.com' for key 'users.email'",
                errno=1062,
                sqlstate='23000'
            )

            # Dati di esempio per la registrazione
            data = {
                'name': 'Test User',
                'email': 'MarioMario@gmail.com',
                'password': 'password123'
            }

            # Chiamata POST al nostro endpoint di registrazione
            response = self.app.post(self.base_url, json=data)
            
            # Verifica che la risposta sia 409 Conflict
            self.assertEqual(response.status_code, 409)
            self.assertIn('Email gi\\u00e0 esistente', response.data.decode('utf-8'))

    
    
    def test_invalid_email_registration(self):
        self.invalid_email_data = {
            'name': 'Test User',
            'email': 'invalidemail.com',  # Email senza chiocciola
            'password': 'TestPassword123'
        }
        response = requests.post(self.base_url, json=self.invalid_email_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email non valida. Deve contenere una chiocciola.', response.json()['error'])


if __name__ == '__main__':
    unittest.main()