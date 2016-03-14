
--    DESCRIPTION

--      mysql --host=10.11.60.191 --user=root --password="tree3" --force <eng_drop

DROP DATABASE `myweb`;
DROP User 'myweb'@'localhost';
DROP USER 'admin'@'%';

DROP USER 'admin'@'localhost';

CREATE DATABASE   `myweb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER 'myweb'@'localhost' ;
CREATE USER 'admin'@'%'  IDENTIFIED BY 'adm123';
CREATE USER 'admin'@'localhost'  IDENTIFIED BY 'adm123';


GRANT ALL ON myweb.* TO 'myweb'@'localhost';
-- GRANT SELECT ON db2.invoice TO 'admin'@'localhost';
-- GRANT USAGE ON *.* TO 'admin'@'localhost' WITH MAX_QUERIES_PER_HOUR 90;

GRANT USAGE ON * . * TO 'myweb'@'localhost' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 100 MAX_UPDATES_PER_HOUR 100 MAX_USER_CONNECTIONS 100 ;


GRANT ALL PRIVILEGES ON `myweb`.* TO 'admin'@'%' WITH GRANT OPTION ;
GRANT ALL PRIVILEGES ON myweb.* TO 'admin'@'localhost' WITH GRANT OPTION;






-- CREATE DATABASE box_django;
-- CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';

-- GRANT ALL PRIVILEGES ON box_django.* TO 'box'@'localhost';

COMMIT;
