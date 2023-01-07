install:
	poetry install

dev:
	python3 manage.py runserver

PORT ?= 8000
start:
	python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	python3 manage.py shell

makemig:
	poetry run python3 manage.py makemigrations

mig:
	poetry run python3 manage.py migrate

trans:
	django-admin compilemessages

lint:
	poetry run flake8 task_manager

tests:
	poetry run python3 manage.py test

tests-cov:
	poetry run coverage run ./manage.py test
	poetry run coverage xml