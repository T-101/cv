.PHONY: build run stop up

BASE_DIR = $(shell pwd)

build:
	@docker build -t cv_backend .

bash:
	@docker run --rm -it --env-file=.env -p 127.0.0.1:8000:8000 -v ${BASE_DIR}/app:/code/app --name cv_backend cv_backend bash

up:
	@docker run --rm -t --env-file=.env -p 127.0.0.1:8000:8000 -v ${BASE_DIR}/app:/code/app --name cv_backend cv_backend
