Apt-get install nginx
Edit /etc/nginx/site-availables/defaut as attached file in same folder with this document.
Replace location with

    location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		proxy_pass http://127.0.0.1:8069;
                proxy_redirect off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                client_max_body_size 200M;
	}

	location /longpolling {
                proxy_pass http://127.0.0.1:8072;
        }

Service nginx restart
apt-get install python-pip
pip install psycogreen
if install odoo 9.0 via deb package, then you have to restore openerp-gevent file (see#10207):
https://github.com/it-projects-llc/odoo-development/blob/master/docs/admin/longpolling.rst
cd /usr/bin/
wget https://raw.githubusercontent.com/odoo/odoo/9.0/openerp-gevent
chmod +x openerp-gevent
Edit /etc/odoo/openerp-server.conf
    xmlrpc_port = 8069
    xmlrpc_interface = 127.0.0.1
    xmlrpc = True
    workers = 6
    proxy_mode = 1
    longpolling_port = 8072
Service odoo restart
Check this line in log file:
Evented Service (longpolling) running on 127.0.0.1:8072

