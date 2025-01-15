#!/bin/sh

alembic upgrade head

gunicorn -c gunicorn.conf.py main:app