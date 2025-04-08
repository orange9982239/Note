# mysql

``` yaml
services:
  mysql:
    container_name: mysql
    image: mysql:5.7
    volumes:
      - /srv/mysql/data:/var/lib/mysql
    ports: 
      - 3306:3306
    environment: 
      - MYSQL_HOST=mysql
      - MYSQL_ROOT_PASSWORD=<<dbpassword>>
      - TZ=Asia/Taipei
  phpmyadmin:
    container_name: phpmyadmin
    depends_on:
      - mysql
    image: phpmyadmin/phpmyadmin
    restart: always
    ports:
      - '80:80'
    environment:
      PMA_HOST: mysql
      MYSQL_ROOT_PASSWORD: <<dbpassword>> 
```