
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --silent

COPY . .
RUN npm run build

# Этап 2: раздача через nginx
FROM nginx:alpine

# Копируем сгенерированную статику в папку nginx
COPY build/ /usr/share/nginx/html/

# Копируем конфиг для поддержки client-side routing
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80