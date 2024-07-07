FROM python:3.12
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY ./models /code/models
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "80"]
