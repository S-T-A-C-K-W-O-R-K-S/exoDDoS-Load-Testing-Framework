FROM locustio/locust:1.0.3

WORKDIR /exoDDoS
COPY . .

CMD ["--config", "exoddos.conf"]
