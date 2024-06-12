# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro nel container
WORKDIR /Authentication

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il contenuto della directory corrente nella directory di lavoro
COPY . .

# Espone la porta su cui l'app Flask girerà
EXPOSE 5002

# Comando per eseguire l'app Flask
CMD ["python", "AuthService.py"]
