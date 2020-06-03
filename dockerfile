FROM locustio/locust:0.14.6

WORKDIR /exoDDoS
COPY . .

CMD ["locust", "-f", "exoddos.py"]
