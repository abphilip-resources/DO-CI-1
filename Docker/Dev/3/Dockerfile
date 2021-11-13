FROM node:14.18.1-alpine3.14
WORKDIR /client

COPY package*.json /client/

RUN npm install

COPY . /client/

EXPOSE 3000

CMD ["npm", "start"]