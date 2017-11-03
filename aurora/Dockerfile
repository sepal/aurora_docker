FROM python:3.4

RUN apt-get update \
  && apt-get install -y libjpeg-dev zlib1g-dev uwsgi uwsgi-plugin-python3 python3-redis

COPY uwsgi.ini /etc/uwsgi.ini

RUN mkdir -p /app/code
WORKDIR /app/code

ONBUILD COPY . /app/code

# Install the requirements, the PlagCheck app has to build its own module
ONBUILD RUN pip install -r requirements_dev.txt \
  && pip install -r PlagCheck/requirements.txt  \
  && pip install psycopg2 \
  && cd PlagCheck/hashing/sherlock \
  && python setup.py install

COPY local_settings.py local_settings.py
#ONBUILD COPY slide_settings.py Slides/settings.py
LABEL dork.root="/app/code"
LABEL dork.hotcode="./"

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
