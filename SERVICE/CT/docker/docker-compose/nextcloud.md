# nextcloud

``` yaml
services:
  nextcloud_db:
    container_name: nextcloud_db
    image: mariadb
    restart: always
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW --innodb_read_only_compressed=OFF
    volumes:
      - /srv/nextcloud/mysql:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=<<dbpassword>>
      - MYSQL_PASSWORD=<<dbpassword>>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - NEXTCLOUD_TRUSTED_DOMAINS=#DomainName#
  nextcloud_ap:
    container_name: nextcloud_ap
    image: nextcloud
    restart: always
    ports:
      - 5000:80
    volumes:
      - /srv/nextcloud/html:/var/www/html
    environment:
      - MYSQL_PASSWORD=<<dbpassword>>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_HOST=nextcloud_db
```