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

test:
	poetry run coverage run ./manage.py test && coverage report
	poetry run coverage xml