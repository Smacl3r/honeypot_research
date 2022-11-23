FROM python:3.12.0a2-alpine3.16

RUN apk update && apk add docker musl-dev linux-headers gcc

RUN mkdir ./app
COPY requirements.txt ./app

WORKDIR ./app

RUN pip install -r requirements.txt
RUN apk add tcpdump
COPY . ./app

EXPOSE 2375

CMD [ "python", "./app/Whaler.py" ]