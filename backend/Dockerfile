FROM python:3.11-alpine3.17

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app/

# to change this default, build using --build-arg timezone=Something/Else
ARG timezone=Europe/Helsinki

RUN apk update \
    && apk add gcc python3-dev musl-dev \
	&& apk add nano tzdata bash \
    && apk add zlib-dev jpeg-dev

ENV TZ=${timezone}

COPY app/requirements.txt /app/
RUN pip install -r requirements.txt
