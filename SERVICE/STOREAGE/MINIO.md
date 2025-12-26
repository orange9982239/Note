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
      MINIO_ROOT_USER: <<minioaccount>>                 # 管理後台用戶名
      MINIO_ROOT_PASSWORD: <<miniopassword>>            # 管理後台密碼，最小8個字符
    volumes:
      - /srv/minio/data:/data                           # 映射當前目錄下的data目錄至容器內/data目錄
      - /srv/minio/config:/root/.minio/                 # 映射配置目錄
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


## nginx
> 通常會用nginx掛fqdn名稱方便操作
1. 管理
  > minio-console.orange.home
1. API
  > minio.orange.home

## CLIENT
### 安裝mc
1. 手動
   1. 下載mc.exe
   2. 複製到 C:\Windows\System32
2. winget
   ```ps1
   winget install MinIO.Client
   ```


## 設定
```sh
# 建立alias
mc alias set minio-orange http://minio.orange.home {ACCESS_KEY} {SECRET_KEY} --insecure

# 測試連線
mc ls minio-orange/my-bucket
```


## 限制access token權限
1. server端配置
  1. ui
     1. 新增access token
        > 自己保存，alias set會用到
     2. 指定權限
           ```json
           {
               "Version": "2012-10-17",
               "Statement": [
                   {
                       "Effect": "Allow",
                       "Action": [
                           "s3:GetBucketLocation",
                           "s3:ListBucket"
                       ],
                       "Resource": [
                           "arn:aws:s3:::my-bucket"
                       ]
                   },
                   {
                       "Effect": "Allow",
                       "Action": [
                           "s3:GetObject"
                       ],
                       "Resource": [
                           "arn:aws:s3:::my-bucket/*"
                       ]
                   }
               ]
           }
           ```
