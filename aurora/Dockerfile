FROM python:3.4.4
RUN mkdir -p /app/code
WORKDIR /app/code
ADD ./source/ /app/code
RUN echo test
RUN sed -i s/wsgiref==0.1.2// requirements.txt
RUN pip install -r requirements.txt
COPY source/local_settings.example.py local_settings.py
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
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
