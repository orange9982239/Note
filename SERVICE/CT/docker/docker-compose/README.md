# 簡述docker-compose
1. 這東西以yaml格式定義docker配置，用起來有點像武功秘笈，配合portainer後非常方便
2. 左邊外面右邊裡面
3. 通常喜歡把volume對應到外層LINUX的`/srv/<<專案>>`路徑上，方便進行rsync備份，可參閱[volumes](#volumes)。

# CONFIG yaml常用的設定
## container_name
> 在容器運行時設置容器的實際名稱
## image
> docker hub上的image tag
## ports
> `外面OS`的PORT對應`CONTAINER內部`的PORT
## environment
> 環境變數，參考該docker image的document
## volumes
> `外面OS`的目錄對應`CONTAINER內部`的目錄，也能用來掛cifs或sftp
``` yaml
volumes:
  cifs:
    driver_opts:
    type: cifs
    o: "username=<<cifsaccount>>,password=<<cifspassword>>"
    device: "//192.168.1.1/<<sharefolder>>"
```
## command
> 似乎是啟動container後下指令用的，可以用來包`npm run`、`dotnet run`...之類的指令
## user
## privileged
> 使用該參數container內的root擁有真正的root權限，否則，container內的root只是外部的一個普通用戶權限。
## hostname
> 只是設置容器認為它自己的主機名
## restart
> 重啟原則
1. no: 不要自動重啟容器。（默認）
2. on-failure：如果容器因錯誤退出，則重新啟動容器，這表現為非零退出代碼。
3. always：如果容器停止，請始終重新啟動容器。如果是手動停止的，只有在 Docker daemon 重啟或者容器本身手動重啟時才會重啟。（請參閱重啟策略詳細信息中列出的第二個項目符號）
4. unless-stopped: 類似於always，除了當容器停止（手動或其他方式）時，即使在 Docker 守護進程重新啟動後它也不會重新啟動。
* ref 
    * https://ithelp.ithome.com.tw/articles/10267079

# REF
* https://blog.gurucomputing.com.au/doing-more-with-docker/deploying-outline-wiki/
* https://docs.docker.com/compose/compose-file/compose-file-v3/#domainname-hostname-ipc-mac_address-privileged-read_only-shm_size-stdin_open-tty-user-working_dir