FROM python:3.4.4
RUN mkdir -p /app/code
WORKDIR /app/code

ONBUILD COPY . /app/code

# Install the requirements, the PlagCheck app has to build its own module
ONBUILD RUN pip install -r requirements.txt \
  && pip install -r PlagCheck/requirements.txt  \
  && cd PlagCheck/hashing/sherlock \
  && python setup.py install

ONBUILD COPY local_settings.py local_settings.py
#ONBUILD COPY slide_settings.py Slides/settings.py
LABEL dork.root="/app/code"
LABEL dork.hotcode="./"

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
