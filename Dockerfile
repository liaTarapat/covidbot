# Verwende ein Python-Basisimage
FROM python:3.9

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anwendungsabhängigkeiten in den Container
COPY requirements.txt .

# Installiere die Anwendungsabhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Anwendungscode in den Container
COPY . .

# Definiere den Befehl, der beim Starten des Containers ausgeführt wird
CMD ["python", "roni.py"]
