import unittest
import requests

class TestSearchEvents(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5003/events'

    def test_search_events_with_valid_query(self):
        # Simula una richiesta di ricerca eventi con una query valida
        response = requests.post(self.base_url, json={'eventName': 'Evento'})
        # Verifica che la risposta sia corretta
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)  # Verifica che la risposta sia una lista

    def test_search_events_with_invalid_query(self):
        # Simula una richiesta di ricerca eventi con una query non valida
        response = requests.post(self.base_url, json={'invalidKey': 'InvalidQuery'})
        # Verifica che la risposta sia corretta
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Query non valida')

if __name__ == '__main__':
    unittest.main()
