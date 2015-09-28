FROM redis:3.0.4

RUN usermod -u 1000 redis
RUN usermod -G staff redis

EXPOSE 6379

VOLUME  ["./data", "/var/lib/redis"]

RUN chown redis /var/lib/redis
