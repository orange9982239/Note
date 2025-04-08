# mssql

## Mssql
``` yaml
services:
  mssql:
    container_name: mssql
    user: root
    image: "mcr.microsoft.com/mssql/server:2019-latest"
    restart: always
    ports:
      - "1433:1433"
    environment:
      SA_PASSWORD: "<<dbpassword>>"
      ACCEPT_EULA: "Y"
      MSSQL_PID: "Express"
    volumes:
      - "smb:/var/opt/mssql/share"
      - "/srv/mssql:/var/opt/mssql"
volumes:
  smb:
    driver_opts:
    type: cifs
    o: "username=<<cifsaccount>>,password=<<cifspassword>>"
    device: "//192.168.1.1/enroll"
```