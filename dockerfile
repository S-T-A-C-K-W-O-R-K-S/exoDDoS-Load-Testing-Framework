FROM locustio/locust:1.2.3

WORKDIR /exoDDoS
COPY . .

CMD ["--config", "exoddos.conf"]
