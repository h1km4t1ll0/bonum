FROM ubuntu
RUN apt update -y &&  apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y nginx python3 python3-pip gunicorn sudo net-tools nano postgresql-contrib libpq-dev
COPY .. /srv/telegram_admin
WORKDIR /srv/telegram_admin
RUN pip3 install -r requirements.txt && cp /srv/telegram_admin/nginx.conf /etc/nginx/sites-available/default
RUN chown -R www-data:www-data /srv && chmod +x /srv/telegram_admin/run.sh && chmod +x /srv
EXPOSE 88:88
# ENTRYPOINT /srv/telegram_admin/run.sh
