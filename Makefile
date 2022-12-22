dev:
	python3 manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn task_manager.wsgi