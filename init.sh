
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s  /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunic_dj.conf   /etc/gunicorn.d/test_dj
sudo /etc/init.d/gunicorn restart
