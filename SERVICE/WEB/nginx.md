# nginx

## 找設定檔案
* 主要設定檔 /etc/nginx/nginx.conf
* 其他設定檔 (可以從主要設定檔內include的路徑來查找)
    * /etc/nginx/conf.d/
    * /etc/nginx/site-enable/
    * /etc/nginx/site-available/

## 開源版 nginx.conf 文件結構
* 簡述結構
    ```conf
    #全域
    events {         
        # 網路連接相關設定
    }

    http {
        # 多個server設定 日誌 請求設定等   
        server { 
            # server內相關參數
            location [PATTERN] {
                # 設定請求的路由與各頁面處理情形
            }
            location [PATTERN] {
                # 設定請求的路由與各頁面處理情形
            }
        }
        server {
            ...
        }    
    }
    ```
* 完整設定
    ```conf
    user nobody nobody;
    # 使用者名稱，使用 ps aux 查看 process會顯示這個名稱，預設為nobody nobody

    worker_processes auto;
    # Nginx的執行緒數量（建議為機器CPU數量x2）

    pid /run/nginx.pid;
    # Nginx的執行緒pid位址

    include /etc/nginx/modules-enabled/*.conf;
    # 讀取 ./modules-enabled/ 內的設定檔

    error_log log/error.log debug;
    # 自訂日誌路徑、級別，可以放在全域、http和server。種類有debug.info.notice.warn.error.crit.alert.emerg等。


    # events 區塊，負責處理每個網路連接
    events {
        worker_connections 768;
        # 每個執行緒同一時間允許的連線總數量

        # multi_accept on;
        # 是否可以接受多個執行緒
        
        accept_mutex on;
        
        #use epoll;
        
    }

    # http 區塊，負責處理透過http協定的連結
    http {

        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # SSL Settings
        ##

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;

        ##
        # Logging Settings
        ##

        access_log /var/log/nginx/access.log;
    # Access log 檔案存放位置
        error_log /var/log/nginx/error.log;
    # log 檔案存放位置

        ##
        # Gzip Settings
        ##

        gzip on;

        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }

    # http 區塊，負責處理透過mail協定的連結，目前註解掉了
    #mail {
    #	# See sample authentication script at:
    #	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
    #
    #	# auth_http localhost/auth.php;
    #	# pop3_capabilities "TOP" "USER";
    #	# imap_capabilities "IMAP4rev1" "UIDPLUS";
    #
    #	server {
    #		listen     localhost:110;
    #		protocol   pop3;
    #		proxy      on;
    #	}
    #
    #	server {
    #		listen     localhost:143;
    #		protocol   imap;
    #		proxy      on;
    #	}
    #}
    ```
## cli
    ```bash
    # 驗證配置nginx.conf
    nginx -t

    # 查看Nginx版本
    nginx -v

    # 啟動
    start nginx

    # 停止
    nginx -s stop
    nginx -s quit

    # 重新載入nginx
    nginx -s reload

    # 打開日誌文件
    nginx -s reopen
    ```
## REF
* https://hackmd.io/@winnienotes/SymsGlMfj