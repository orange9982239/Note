# gitea
``` yaml
version: "3"
services:
  gitea:
    container_name: gitea
    image: gitea/gitea:1.13.1
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    volumes:
      - /srv/gitea/data:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "22:22"
```