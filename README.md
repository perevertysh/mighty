# Simple grader, providing some buisness logic for add code in form and push it for check

for start app you need

install nginx, gunicorn, node.js, npm

install redis by docker:

	sudo docker run -d -p 6379:6379 redis

prepare enviroment file (.env) in dir 'mighty/':
	
	*postgres*	
	DB_NAME='databasee name'
	DB_USER='database username'
	DB_PASSWORD='database username password'
	DB_HOST='database host'
	DB_PORT='database port'
	*app*
	HOST='your app host
	DEBUG='luanch mode True/False'
	MEDIA_ROOT=/var/www/'app name'/
	PROJECT='app name'
	SECRET_KEY='your secret key'

prepare enviroment file (.env) in dir bin/:
	
	PROJECT=*project name*
	USERNAME=*user name*	
	
create python virtual enviroment, install dependencies from with pip requirements.txt

execute commands (from virtual environment) in different terminal windows:

	python ./bin/start_app.py - luanch app
	python ./bin/start_celery.py - luanch celery

with 'start_app' command:

	symlinks are created for the nginx configuration,
	sets the directory for storing image files in nginx
	running nginx
	building frontend (Vue.js)
	building django statics
	django migrations to db
	gunicorn launch
