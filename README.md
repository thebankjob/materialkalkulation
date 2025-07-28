# Materialkalkulation

## Voraussetzungen
- Docker + Docker Compose

## Start

1. Kopiere die Datei `.env.example` nach `.env` und passe die Werte bei Bedarf an (Standardwerte funktionieren im Docker Compose)
2. Im Projektordner: `docker compose up --build` (verwendet `docker-compose.yml`)
3. Frontend läuft auf [http://localhost:3300](http://localhost:3300)
   Backend auf [http://localhost:8096](http://localhost:8096)

Die Container können auch bequem über Portainer erstellt werden. Die
Dockerfiles erwarten die Umgebungsvariable `REACT_APP_API_URL`, welche
standardmäßig im Compose-Setup auf `http://backend:8000` gesetzt ist.
