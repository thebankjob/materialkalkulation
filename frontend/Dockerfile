# frontend/Dockerfile

FROM node:20

WORKDIR /app

# Set build-time environment variable for API URL
ARG REACT_APP_API_URL=http://backend:8000
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# Installiere Abhängigkeiten
COPY package.json ./
RUN npm install

# Kopiere den restlichen Frontend-Code
COPY . ./

# Baue das React-Frontend
RUN npm run build

# Installiere einen Produktions-Webserver (serve)
RUN npm install -g serve

# Exponiere Port 3000
EXPOSE 3000

# Starte die gebaute React-App auf Port 3000
CMD ["serve", "-s", "build", "-l", "3000"]