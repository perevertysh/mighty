import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

username = env("USERNAME")
project = env('PROJECT')

if not os.path.islink(f"/etc/nginx/sites-enabled/{project}.conf"):
    os.system("sudo rm /etc/nginx/sites-enabled/default")
    os.system(f"sudo mkdir /var/www/{project}")
    os.system(f"sudo chown {username} /var/www/{project}")
    os.system(f"sudo ln -s {path}/nginx/{project}.conf "
              f"/etc/nginx/sites-enabled/")
os.system("sudo service nginx restart")
os.system(f"cd {path}/frontend; npm install; npm run production")
os.system("python manage.py collectstatic --noinput")
os.system("python manage.py migrate")
os.system("python manage.py loaddata checker/fixtures/data.json")
os.system(f"exec gunicorn  -c '{path}/bin/gunicorn-config.py' {project}.wsgi")
