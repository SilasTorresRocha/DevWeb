FROM node:20-alpine

WORKDIR /app

# Instala as dependências primeiro para aproveitar o cache do Docker
COPY package*.json ./
RUN npm install

# Copia o restante do código da aplicação
COPY . .

EXPOSE 8000

# Executa o servidor de desenvolvimento do Next.js
CMD ["npm", "run", "dev"]
