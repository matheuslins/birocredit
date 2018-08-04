DOCKER_COMPOSE=docker-compose.yml

build:
	@sudo docker-compose -f $(DOCKER_COMPOSE) build

up:
	@sudo docker-compose -f $(DOCKER_COMPOSE) up

run:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web

down:
	@sudo docker-compose -f $(DOCKER_COMPOSE) down

setup:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web python3 manage.py makemigrations; python3 manage.py migrate

merge:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web python3 manage.py makemigrations --merge

user:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web python3 manage.py createsuperuser

shell:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web python3 manage.py shell

app:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web python3 manage.py startapp $(n)

migra:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web python3 manage.py makemigrations $(n); python3 manage.py migrate $(n)

web:
	@sudo docker-compose -f $(DOCKER_COMPOSE) run web /bin/bash

clean: clean-build clean-others clean-pyc clean-test

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-others:
	@find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/