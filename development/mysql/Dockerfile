FROM mysql:5.7

RUN usermod -u 1000 mysql
RUN usermod -G staff mysql
RUN chown mysql /var/run/mysqld

EXPOSE 3306

#mysql --user="root" --password="6bzR3WuY13tXaVXn7ICWtCEE2ei5Llkz" \
#  --database="events" \
#  --execute="GRANT ALL PRIVILEGES ON events.* TO 'events'@'%' IDENTIFIED BY 'y4hU8m0J8rVxKXoDNXdKL0R9tkyiHxDd'"

# Modified so that we can connect with Hibernate, due to the following issue in MySQL:
# http://stackoverflow.com/a/32054183/974800
RUN echo "show_compatibility_56=1" >> /etc/mysql/my.cnf
