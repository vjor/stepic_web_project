sudo  /etc/init.d/mysql start

sudo mysql -uroot   --force < cr_db01.sql  > cr_db.log
#sudo  /etc/init.d/mysql restart
