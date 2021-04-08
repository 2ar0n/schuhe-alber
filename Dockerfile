FROM alpine:3.13

RUN apk add --no-cache --update npm

WORKDIR /tmp/site

RUN npm update
RUN npm install tailwindcss@latest postcss@latest autoprefixer@latest
