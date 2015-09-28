Docker Base App

A ready to go docker app with:
- MySQL
- Redis for caching
- Nginx
- uwsgi
- Python
- Flask

The basic Flask app has:
- Sample user registration and login
- Saving to MySQL
- Basic templates
- Flask Debug Toolbar
- Well structured modular flask app

Some other features include:
- Development, Testing and Production modes
- Quick auto-reloading of code while working in development mode

Instructions for running
- Download docker toolbox from https://www.docker.com/toolbox
- Setup a virtualbox machine called dev
- ```dm create -d virtualbox --engine-opt dns=8.8.8.8 dev```
- The dns=8.8.8.8 helped me run pip install commands inside the container from captive WiFi portals
- Clone the git repository
- Change the mysql passwords in common/docker-compose.yml
- Run the following commands
- ```cd development```
- ```docker-compose up -d```
- ```docker exec -it web-dev /bin/bash```
- ```cd /var/www/events```
- ```sh setup_app.sh```
- ```dm inspect -f '{{ .Driver.IPAddress }}' dev```

At this point you should be able to open a web browser and point to the ip (port 8080) received from the last command and see the site. For example if the ip was 192.168.99.101 then point to http://192.168.99.101:8080
