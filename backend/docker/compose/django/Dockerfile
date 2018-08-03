FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django

RUN mkdir -p /app
COPY . /app
RUN chown -R django /app

WORKDIR /app

RUN mkdir -p /app/staticfiles
RUN chown -R django:django /app/staticfiles

RUN mkdir -p /app/medias
RUN chown -R django:django /app/media

RUN mkdir -p /home/django
RUN chown -R django:django /home/django

VOLUME /app/media
VOLUME /app/staticfiles
