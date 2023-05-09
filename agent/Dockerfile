FROM python:3-alpine

RUN apk update && apk add docker musl-dev linux-headers gcc libpcap-dev tcpdump

RUN mkdir /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install Cython
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 2375

CMD [ "python", "/app/Whaler.py" ]