FROM python:3.12.1-alpine3.19

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

# to change this default, build using --build-arg timezone=Something/Else
ARG timezone=Europe/Helsinki
ENV TZ=${timezone}

RUN apk update \
    && apk add gcc python3-dev musl-dev \
	&& apk add nano tzdata bash \
    && apk add zlib-dev jpeg-dev

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
