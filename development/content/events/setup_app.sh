#!/bin/sh

/opt/virtualenv/bin/python manage.py create_db
/opt/virtualenv/bin/python manage.py db init
#/opt/virtualenv/bin/python manage.py db migrate
/opt/virtualenv/bin/python manage.py create_admin
/opt/virtualenv/bin/python manage.py create_data
