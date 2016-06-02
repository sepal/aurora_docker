FROM python:3.4.4
RUN mkdir -p /app/code
WORKDIR /app/code
ADD ./source/ /app/code

# Install the requirements, the PlagCheck app has to build its own module
RUN pip install -r requirements.txt \
  && pip install -r PlagCheck/requirements.txt  \
  && cd PlagCheck/hashing/sherlock \
  && python setup.py install

COPY local_settings.py local_settings.py
COPY slide_settings.py Slides/settings.py

# Create the media and static dirs.
RUN mkdir -p /app/media \
  && mkdir -p /app/static

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
