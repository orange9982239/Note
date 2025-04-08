## code-server
``` yaml 
version: "3"
services:
  codeserver:
    container_name: code-server
    image: codercom/code-server
    ports:
      - "6000:8080"
    volumes:
      - "/usr/local/code-server/project:/home/coder/project"
    environment:
      PASSWORD: "<<password>>"
    restart: always
    user: "0:0"
```