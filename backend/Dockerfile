FROM python:3.13.1-alpine3.21

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apk update \
    && apk add gcc python3-dev musl-dev \
	&& apk add nano tzdata bash \
    && apk add zlib-dev jpeg-dev

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
