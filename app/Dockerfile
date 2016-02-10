FROM python:3.4.4-alpine
RUN mkdir /app
WORKDIR /app
ADD ./source
RUN pip install -r requirements.txt
COPY local_settings.example.py /code/local_settings.py
RUN sed -i s:/vagrant/:/app/: local_settings.py \
  && sed -i s/django.db.backends.sqlite3/postgresql_psycopg2/ source/AuroraProject/settings.py \
  && sed -i s/database.db/aurora/ source/AuroraProject/settings.py \
  && sed -i s/"'USER': 'root'"/"'USER': 'aurora'"/ source/AuroraProject/settings.py \
  && sed -i s/"'PASSWORD': 'root'"/"'PASSWORD': {DB_PASSWORD}"/ source/AuroraProject/settings.py \
  && sed -i s/"'HOST': 'localhost'"/"'HOST': 'db'"/ source/AuroraProject/settings.py \
  && sed -i s/"'PORT': '8080'"/"'PORT': '5432'"/ source/AuroraProject/settings.py
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
