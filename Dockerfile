FROM ubuntu
RUN apt update -y
RUN apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y nginx python3 python3-pip gunicorn cron sudo net-tools nano postgresql-contrib libpq-dev
# libpq-dev
# RUN DEBIAN_FRONTEND=noninteractive apt install -y postgresql postgresql-contrib libpq-dev
COPY ./ /srv/telegram_admin
WORKDIR /srv/telegram_admin
# RUN service postgresql start && sudo -u postgres psql -f psql
RUN pip3 install -r requirements.txt && cp /srv/telegram_admin/nginx.conf /etc/nginx/sites-available/default
# RUN python3 manage.py collectstatic --noinput
# RUN python3 manage.py migrate
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate
# RUN python3 manage.py initadmin
# RUN service nginx start
RUN chown -R www-data:www-data /srv/telegram_admin && chmod +x /srv/telegram_admin/run.sh
EXPOSE 88:88
ENTRYPOINT /srv/telegram_admin/run.sh
