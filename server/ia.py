# Esegui questo script separatamente dal progetto Angular
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random

# Dizionario delle domande e delle risposte del chatbot
domande_risposte = {
    "Come stai?": ["Sto bene, grazie!", "Tutto bene, tu?", "Non c'è male, e tu?"],
    "Qual è il tuo nome?": ["Mi chiamo ChatBot.", "Sono conosciuto come ChatBot."],
    "Che tempo fa oggi?": ["Sembra che sia una giornata soleggiata!", "Fa caldo oggi!"],
    "Cosa fai nel tempo libero?": ["Mi piace chattare con persone come te!", "Mi diverto ad imparare cose nuove."],
    "Hai qualche hobby?": ["Mi piace leggere e imparare cose nuove.", "Mi piace conversare con persone interessanti."],
    "Qual è il senso della vita?": ["La risposta potrebbe sorprenderti!", "Potrebbe essere una domanda profonda..."],
    "Cosa mangi?": ["Non mangio nulla, sono solo un programma.", "Non ho bisogno di cibo, grazie!"]
}

# Funzione che restituisce una risposta del chatbot
def chatbot_risposta(domanda):
    if domanda in domande_risposte:
        return random.choice(domande_risposte[domanda])
    else:
        return "Mi dispiace, non ho una risposta per quella domanda."

# Classe che gestisce le richieste HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        domanda = data.get('domanda', '')
        risposta = chatbot_risposta(domanda)
        response_data = {'risposta': risposta}
        response = json.dumps(response_data["risposta"]).encode('utf-8')
        print(response_data['risposta'])
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:4200')  # Imposta il dominio del frontend
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        self.send_response(405)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Metodo non consentito. Si prega di utilizzare le richieste POST.')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def run_server():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server is running on http://localhost:3000")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
