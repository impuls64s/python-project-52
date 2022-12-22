dev:
	python3 manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi