# MINIO

## SERVER
### 建置
``` yaml 
services: 
  minio:
    image: minio/minio
    container_name: minio
    restart: always
    ports:
      - 9000:9000    # API端口
      - 9001:9001    # 管理端口
    command: server /data --console-address ':9001' --address ':9000'
    environment:
      MINIO_ROOT_USER: <<minioaccount>>                 #管理后台用户名
      MINIO_ROOT_PASSWORD: <<miniopassword>>            #管理后台密码，最小8个字符
    volumes:
      - /srv/minio/data:/data                           #映射当前目录下的data目录至容器内/data目录
      - /srv/minio/config:/root/.minio/                 #映射配置目录
```
### 掛載SMB
```yaml
volumes:
  smb:
  driver_opts:
  type: cifs
  o: "username=<<cifsaccount>>,password=<<cifspassword>>"
  device: "//192.168.1.1/minio"
```

### 管理端口使用
1. 登入管理端口
   * http://192.168.0.1:9001
2. bucket
   1. 建立bucket
   2. 管理bucket權限
   3. 上傳/下載檔案

### API端口使用
4. API端口取檔案
    * 桶名稱    => http://192.168.0.1:9001 #API端口直接進入的話，他會轉導到管理端口
    * 桶名稱    => test
    * 檔案名稱  => A13.pdf
    * 檔案url   => http://192.168.0.1:9001/test/A13.pdf





## CLIENT
### 安裝mc
1. 下載mc.exe
2. 複製到 C:\Windows\System32

## 設定
```sh
mc config host add {serverAliasName} {URL} {ACC} {PW}
mc config host add minio-server http://192.168.1.1:9000 #account# #password#
```

## 操作
1. 列出所有桶
```sh
mc tree {serverAliasName}
mc tree minio-server
```
