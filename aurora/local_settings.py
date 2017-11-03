# Use other paths if you intend to run this without vagrant
MEDIA_ROOT = '/app/media'
STATIC_ROOT = '/app/static'

MEDIA_URL = '/media/'

# Use %%NEXT_URL%% pattern inside SSO_URI to replace it with
# the previously requested url to get redirected to it after
# a successfull SSO auth.
SSO_URI = '/temporary_uri/?param=%%NEXT_URL%%'

LECTURER_USERNAME = 'lecturer'
LECTURER_SECRET = 'lecturersecret'

SSO_SHARED_SECRET = 'ssosecret'

AUTHENTICATION_BACKENDS = (
  'middleware.AuroraAuthenticationBackend.AuroraAuthenticationBackend',
  'django.contrib.auth.backends.ModelBackend',
)

ALLOWED_HOSTS = ['aurora.dork.io']

CHANNEL_LAYERS = {
  "default": {
    "BACKEND": "asgi_redis.RedisChannelLayer",
    "CONFIG": {
      "hosts": [("redis", 6379)],
    },
    "ROUTING": "AuroraProject.routing.channel_routing",
  }
}

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'aurora',
    'USER': 'aurora_dbuser',
    'PASSWORD': 'nosecret',
    'HOST': 'localhost',
    'PORT': '',
  },
  'plagcheck': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'plagcheck',
    'USER': 'aurora_dbuser',
    'PASSWORD': 'nosecret',
    'HOST': 'localhost',
    'PORT': '',
  },
}
