### Deployment Instructions for Flask, Gunicorn, and Nginx

Most of the deployment was done by following [these instructions](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04).

Ensure you have `gunicorn` and `flask` installed. Both can be installed via `pip`.

The `nginx` and `systemd` files are located in this folder.

##### TL;DR Steps

Perform basic DNS and domain setup. Then, in your server box, run the following commands

```console
$ cd /var/www
$ git clone https://www.github.com/Chris-Johnston/CROBBER
$ cd CROBBER/deployment
$ sudo cp crobber.service /etc/systemd/system
$ sudo systemctl start crobber
$ sudo systemctl enable crobber
$ sudo cp crobber.rodeo /etc/nginx/sites-available
$ cd /etc/nginx/sites-enabled
$ sudo ln -s ../sites-available/crobber.rodeo .
$ sudo systemctl restart nginx
```

If you want HTTPS enforcing, run `certbot` for the domain and restart `nginx` again.
