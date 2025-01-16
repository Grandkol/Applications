#!/bin/sh

alembic revision --autogenerate -m "Initial"
alembic upgrade head

gunicorn -c gunicorn.conf.py main:app