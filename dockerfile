FROM locustio/locust:1.1

WORKDIR /exoDDoS
COPY . .

CMD ["--config", "exoddos.conf"]
