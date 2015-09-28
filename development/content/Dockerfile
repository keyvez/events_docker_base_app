FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install build-essential git python python-dev python-setuptools \
  nginx supervisor libmysqlclient-dev
RUN easy_install pip

run apt-get install -y software-properties-common python-software-properties
run add-apt-repository -y ppa:nginx/stable
run apt-get update
run apt-get install -y sqlite3

RUN mkdir -p /var/log/nginx/events
RUN mkdir -p /var/log/uwsgi/events

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
COPY uwsgi.ini /var/www/

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#COPY events /var/www/events
#RUN pip install -r /var/www/events/requirements.txt

#ENV WORKON_HOME /opt/virtualenv

# Setup virtualenv
RUN pip install virtualenv
RUN virtualenv /opt/virtualenv
RUN . /opt/virtualenv/bin/activate
ENV PYTHON=/opt/virtualenv/bin/python
ENV APP_SETTINGS=project.config.DevelopmentConfig

# Install python requirements in virtualenv
COPY requirements.txt /opt/
RUN /opt/virtualenv/bin/pip install -r /opt/requirements.txt

#WORKDIR /var/www/events
#RUN /opt/virtualenv/bin/python manage.py create_db
#RUN /opt/virtualenv/bin/python manage.py db init
#RUN /opt/virtualenv/bin/python manage.py db migrate
#RUN /opt/virtualenv/bin/python manage.py create_admin
#RUN /opt/virtualenv/bin/python manage.py create_data

EXPOSE 8080

CMD ["/usr/bin/supervisord"]
