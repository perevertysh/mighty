import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# command = '{}/../pettyenv/bin/gunicorn'.format(path)
command = '/usr/local/bin/gunicorn'
pythonpath = '{}'.format(path)
bind = '127.0.0.1:8001'
workers = 5
user = env("USERNAME")
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = f"DJANGO_SETTINGS_MODULE={env('PROJECT')}.settings"
