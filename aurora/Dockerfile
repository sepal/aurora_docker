FROM python:3.4.4
RUN mkdir -p /app/code
WORKDIR /app/code
ADD ./source/ /app/code
RUN echo test
RUN sed -i s/wsgiref==0.1.2// requirements.txt
RUN pip install -r requirements.txt
COPY source/local_settings.example.py local_settings.py

# Change the settings and create the media and static dirs.
RUN sed -i s:/vagrant/aurora/:/app/: local_settings.py \
  && sed -i s/"'ENGINE': 'django.db.backends.sqlite3'"/"'ENGINE': 'django.db.backends.postgresql_psycopg2'"/ AuroraProject/settings.py \
  && sed -i s/database.db/aurora/ AuroraProject/settings.py \
  && sed -i s/"'USER': 'root'"/"'USER': 'aurora'"/ AuroraProject/settings.py \
  && sed -i s/"'PASSWORD': 'root'"/"'PASSWORD': os.environ['POSTGRES_PASSWORD']"/ AuroraProject/settings.py \
  && sed -i s/"'HOST': 'localhost'"/"'HOST': 'db'"/ AuroraProject/settings.py \
  && sed -i s/"'PORT': '8080'"/"'PORT': '5432'"/ AuroraProject/settings.py \
  && cp  Slides/settings.example.py Slides/settings.py \
  && mkdir -p /app/media \
  && mkdir -p /app/static

# Install a testing environment using behave, selenium + phantomjs
ENV DEBIAN_FRONTEND noninteractive
ENV PHANTOM_JS_VERSION 1.9.7-linux-x86_64
RUN apt-get update && apt-get install -y curl bzip2 libfreetype6 libfontconfig \
  && curl -sSL https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_JS_VERSION.tar.bz2 | tar xjC /opt \
  && ln -s /opt/phantomjs-$PHANTOM_JS_VERSION/bin/phantomjs /usr/bin/phantomjs \
  && pip install selenium behave_django factory_boy


EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
