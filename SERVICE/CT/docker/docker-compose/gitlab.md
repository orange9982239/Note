## Gitlab

> 少年不要衝動想衝latest最新版，會哭的
> 穩定才是正道的光 
``` yaml 
version: "3.6"
services:
  gitlab:
    container_name: gitlab
    image: gitlab/gitlab-ce:13.12.15-ce.0 #latest
    restart: always
    privileged: true
    ports:
      - '8080:80'
      - '8443:443'
      - '8022:22'
    volumes:
      - /srv/gitlab/data:/var/opt/gitlab
      - /srv/gitlab/logs:/var/log/gitlab
      - /srv/gitlab/config:/etc/gitlab
```
<!--
# environment:
#   - GITLAB_ROOT_PASSWORD=<<password>>
#   - GITLAB_ROOT_EMAIL=administrator@orange.home 
-->
- ref
  - https://zhuanlan.zhihu.com/p/201097039