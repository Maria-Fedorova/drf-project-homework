FROM python:3

WORKDIR /drf-docker

COPY ./requirements.txt /drf-docker/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]