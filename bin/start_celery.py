import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

username = env("USERNAME")
project = env('PROJECT')
os.system(f"celery worker -A {project} --loglevel=info")
