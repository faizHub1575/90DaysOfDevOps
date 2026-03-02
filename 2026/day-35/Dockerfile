# ---------- Stage 1: Build ----------
FROM node:20 AS builder

WORKDIR /app

COPY package.json .
RUN npm install --production

COPY app.js .

# ---------- Stage 2: Minimal Runtime ----------
FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 3000

CMD ["node", "app.js"]