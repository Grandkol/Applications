FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UVICORN_WORKERS=4


WORKDIR /app
COPY requirements.txt requirements.txt
COPY gunicorn/gunicorn.conf.py .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY ./src .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]