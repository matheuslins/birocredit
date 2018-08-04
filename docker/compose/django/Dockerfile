FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY ./backend/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django

RUN mkdir -p /app/backend
COPY . /app/backend
RUN chown -R django /app/backend

WORKDIR /app/backend

RUN mkdir -p /app/backend/staticfiles
RUN chown -R django:django /app/backend/staticfiles

RUN mkdir -p /app/backend/medias
RUN chown -R django:django /app/backend/media

RUN mkdir -p /home/django
RUN chown -R django:django /home/django

VOLUME /app/backend/media
VOLUME /app/backend/staticfiles
