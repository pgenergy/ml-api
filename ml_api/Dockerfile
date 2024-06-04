
FROM python:3.9
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
COPY ./app /code/app
COPY ./models /code/models

CMD ["uvicorn", "app.main:app", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "80"]
