import unittest
import requests

class TestChatbotServer(unittest.TestCase):
    def setUp(self):
        # Configura l'URL del server locale
        self.base_url = 'http://localhost:3000'

    def test_domanda_conosciuta(self):
        # Invia una domanda conosciuta al server e verifica la risposta
        domanda = 'Come stai?'
        expected_risposta = ['Sto bene, grazie!', 'Tutto bene, tu?', "Non c'è male, e tu?"]

        response = requests.post(self.base_url, json={'domanda': domanda})
        self.assertEqual(response.status_code, 200)

        # Debug: stampa la risposta del server
        print("Risposta ricevuta (domanda conosciuta):", response.text)

        risposta = response.json()
        self.assertIn(risposta, expected_risposta)

    def test_domanda_sconosciuta(self):
        # Invia una domanda sconosciuta al server e verifica la risposta
        domanda = 'Qual è il tuo colore preferito?'
        expected_risposta = "Mi dispiace, non ho una risposta per quella domanda."

        response = requests.post(self.base_url, json={'domanda': domanda})
        self.assertEqual(response.status_code, 200)

        # Debug: stampa la risposta del server
        print("Risposta ricevuta (domanda sconosciuta):", response.text)

        risposta = response.json()
        self.assertEqual(risposta, expected_risposta)

    def test_domanda_simile(self):
        # Invia una domanda conosciuta al server e verifica la risposta
        domanda = 'Come stai'
        expected_risposta = "Mi dispiace, non ho una risposta per quella domanda."

        response = requests.post(self.base_url, json={'domanda': domanda})
        self.assertEqual(response.status_code, 200)

        # Debug: stampa la risposta del server
        print("Risposta ricevuta (domanda conosciuta):", response.text)

        risposta = response.json()
        self.assertIn(risposta, expected_risposta)

if __name__ == '__main__':
    unittest.main()
