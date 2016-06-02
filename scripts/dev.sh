#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py populate_demo_data
