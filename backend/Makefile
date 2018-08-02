run:
	python3 manage.py runserver

setup:
	 python3 manage.py makemigrations
	 python3 manage.py migrate

merge:
	 python3 manage.py makemigrations --merge

user:
	 python3 manage.py createsuperuser

shell:
	 python3 manage.py shell

app:
	 python3 manage.py startapp $(n)

migra:
	 python3 manage.py makemigrations $(n)
	 python3 manage.py migrate $(n)

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