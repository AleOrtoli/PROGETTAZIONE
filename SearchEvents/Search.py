from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import logging

app = Flask(__name__)
CORS(app)

# Configura il logging
logging.basicConfig(level=logging.DEBUG)

# Configura la connessione al database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="192837465",
    database="event_management"
)

@app.route('/events', methods=['POST'])
def search_events():
    # Ottieni i parametri di ricerca dalla richiesta
    data = request.json
    query = data.get('eventName')

    if not query:
        return jsonify({'message': 'Query non valida'}), 400

    try:
        cursor = db.cursor(dictionary=True)
        # Esegui la query per cercare eventi che corrispondono alla query
        logging.debug("Executing query for events with query: %s", query)
        cursor.execute("SELECT * FROM events WHERE name LIKE %s OR event_date LIKE %s", ('%' + query + '%', '%' + query + '%'))
        events = cursor.fetchall()
        cursor.close()

        # Restituisci gli eventi trovati come JSON
        logging.debug("Events found: %s", events)
        return jsonify(events), 200

    except mysql.connector.Error as err:
        logging.error("Error: %s", err)
        return jsonify({'message': 'Errore durante la ricerca degli eventi', 'error': str(err)}), 500

if __name__ == '__main__':
    app.run(port=5003, debug=True)
