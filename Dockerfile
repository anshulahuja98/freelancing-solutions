FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE freelancing-solutions.settings

RUN mkdir /dist
WORKDIR /dist
RUN ls
COPY . /dist/
RUN pip3 install pipenv
RUN pipenv install --system --deploy
WORKDIR /dist/src

