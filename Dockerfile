# Usa un'immagine di base di Node.js per compilare l'app Angular
FROM node:latest AS builder

# Imposta la directory di lavoro
WORKDIR /app

# Copia il package.json e il package-lock.json nella directory di lavoro
COPY package*.json ./

# Installa le dipendenze
RUN npm install

# Copia i file dell'app Angular nella directory di lavoro
COPY . .

# Compila l'app Angular
RUN npm run build

# Utilizza un'immagine di base di Nginx per servire l'app Angular compilata
FROM nginx:alpine

# Copia i file compilati dall'immagine Node.js nella directory di lavoro di Nginx
COPY --from=builder /app/dist/* /usr/share/nginx/html/
