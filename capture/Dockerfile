FROM python:3-alpine

RUN apk add tcpdump

RUN mkdir /app
COPY ./script /app

#ENTRYPOINT ["tail", "-f", "/dev/null"] 
ENTRYPOINT ["/bin/sh","/app/wrapper.sh"]

