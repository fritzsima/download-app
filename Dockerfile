FROM python:3.8

ENV ENV=development

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

RUN mkdir -p /code/static

ENV STATIC_DIR=/code/static/

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]