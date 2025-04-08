# codimd_db
``` yaml
version: "3"
services:
  codimd_db:
    container_name: codimd_db
    image: postgres:11.6-alpine
    environment:
      - POSTGRES_USER=<<dbaccount>>
      - POSTGRES_PASSWORD=<<dbpassword>>
      - POSTGRES_DB=codimd
    volumes:
      - /srv/codimd/postgresql:/var/lib/postgresql/data
    restart: always
  codimd_ap:
    container_name: codimd_ap
    image: hackmdio/hackmd:2.3.2
    environment:
      - CMD_DB_URL=postgres://<<dbaccount>>:<<dbpassword>>@codimd_db/codimd
      - CMD_USECDN=false
      - CMD_ALLOW_ANONYMOUS=false
      - CMD_ALLOW_EMAIL_REGISTER=false
    depends_on:
      - codimd_db
    ports:
      - "3000:3000"
    volumes:
      - /srv/codimd/uploads:/home/hackmd/app/public/uploads
    restart: always
```