FROM node:22-alpine

WORKDIR /app

# Instala as dependências
COPY package*.json ./
RUN npm install

# Copia o restante da aplicação
COPY . .

EXPOSE 3000

# Inicia o servidor Next.js
CMD ["npm", "run", "dev"]
