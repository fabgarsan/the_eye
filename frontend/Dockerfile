FROM node:15-alpine

WORKDIR /usr/src/frontend
COPY package*.json ./

RUN npm i --silent

EXPOSE 8080

CMD ["npm", "run", "serve"]
