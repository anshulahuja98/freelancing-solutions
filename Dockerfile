FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE freelancing-solutions.settings

RUN mkdir /dist
WORKDIR /dist
RUN git clone https://github.com/anshulahuja98/freelancing-solutions /dist && git checkout master

RUN pip3 install pipenv
RUN pipenv install --system --deploy
WORKDIR /dist/src

EXPOSE 8000

RUN chmod +x /dist/entrypoint.sh
ENTRYPOINT ["/dist/entrypoint.sh"]


