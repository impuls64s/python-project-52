dev:
	python3 manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	python3 manage.py shell

makemig:
	poetry run python3 manage.py makemigrations

mig:
	poetry run python manage.py migrate

trans:
	django-admin compilemessages