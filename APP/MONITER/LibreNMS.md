# LibreNMS
## 建置
1. 產出 base64 key
    ```sh
    sudo docker run --rm jarischaefer/docker-librenms generate_key
    # base64:ICIrOcp5lXXXXXXXXXXXXFDg4kVi62o=
    ```
2. 建置服務
    1. create docker-compose.yml
        ```sh
        mkdir /srv/librenms
        vim /srv/librenms/docker-compose.yml
        ```
        ```yml
        services:
          web:
            image: jarischaefer/docker-librenms
            container_name: librenms_web
            restart: always
            ports:
              - '80:80'
            volumes:
              - /srv/librenms/logs:/opt/librenms/logs
              - /srv/librenms/rrd:/opt/librenms/rrd
            environment:
              APP_KEY: base64:ICIrOcp5lXXXXXXXXXXXXFDg4kVi62o=          # base64 key
              DB_HOST: librenms_database
              DB_USER: librenms
              DB_PASS: '!QAZ2wsx'
              DB_NAME: librenms
              POLLERS: 16                                               # cpu core數
              BASE_URL: http://192.168.1.2                              # LAN IP
              TZ: Asia/Taipei
            depends_on:
              - mysql
          mysql:
            image: mariadb:10.5
            container_name: librenms_database
            restart: always
            ports:
              - '3306:3306'
            volumes:
              - /srv/librenms/mysql:/var/lib/mysql
            environment:
              TZ: Asia/Taipei
              MYSQL_ROOT_PASSWORD: '!QAZ2wsx'
              MYSQL_USER: librenms
              MYSQL_PASSWORD: '!QAZ2wsx'
              MYSQL_DATABASE: librenms
        ```
    2. docker-compose建立container
        ```sh
        sudo docker-compose up -d
        ```
    3. LibreNMS初始化設定
        ```sh
        # init DB
        sudo docker exec librenms_web setup_database

        # create admin
        sudo docker exec librenms_web create_admin

        ## 這指令將會建立一個 admin 管理者：
        ## 帳號： admin
        ## 密碼： admin
        ## E-Mail： admin@example.com
        ```
    4. 測試
        1. web
            > http port 80
        2. db
            > mysql port 3306
    5. 參考
        > https://blog.jks.coffee/setup-librenms-using-docker/
## 設定
1. 被監控設備設定
   1. snmp service
      1. 自訂community
      2. os啟用snmp service
         * windows
            1. snmp service安裝
                ```ps1
                # 安裝 SNMP 服務功能
                # 適用於Windows Server
                Install-WindowsFeature -Name "SNMP-Service" -IncludeManagementTools

                # 適用於 Windows 10/11
                Add-WindowsCapability -Online -Name "SNMP.Client~~~~0.0.1.0"

                # 啟動 SNMP 服務
                Start-Service -Name "SNMP"

                # 設置 SNMP 服務為自動啟動
                Set-Service -Name "SNMP" -StartupType Automatic
                ```
            2. 安裝informant-std-17.exe擴充snmp
               * https://www.snmp-informant.com/downloads.htm
            3. 防火牆
               1. 關閉或允許特定IP接收
                  ```ps1
                  New-NetFirewallRule -DisplayName "Allow SNMP Service" -Direction Inbound -Protocol UDP -LocalPort 161 -Action Allow
                  ```
            3. 配置 SNMP community
               ```ps1
               # 設置 SNMP 社群名稱 (例如 "home")
               Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\ValidCommunities" -Name "home" -Value 4 -Type DWord

               # 設置 SNMP 接收封包允許來自主機
               Remove-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\PermittedManagers' -Name *

               # 重啟snmp service
               Restart-Service -Name snmp
               ```
         * linux
            1. snmp service安裝
               1. 安裝
                    ```sh
                    # 安裝
                    sudo apt update
                    sudo apt install snmpd snmp
                    ```
               2. 服務配置
                    ```sh
                    # 改設定
                    sudo vim /etc/snmp/snmpd.conf
                    ```
                    * 設置 SNMP 社群名稱 (例如 "home")
                    ```conf
                    # 設定系統資訊
                    syslocation "Your Location"  # 例如 "Taipei, Taiwan"
                    syscontact Your_Name <your@email.com>  # 系統管理員聯絡資訊

                    # 設定社群名稱 (SNMP community) - 這是 SNMP 的密碼
                    rocommunity home  # 唯讀社群名稱 (建議生產環境改用更安全的字串)
                    # rwcommunity private  # 如需讀寫權限可取消註解 (極不安全，不建議)

                    # 限制存取來源 (建議設定)
                    rocommunity home 192.168.0.0/24     # 只允許特定網段
                    # rocommunity home 127.0.0.1        # 只允許本機

                    # 監聽所有網路介面
                    agentAddress udp:161

                    # 系統資訊存取權限
                    view systemonly included .1.3.6.1.2.1.1
                    view systemonly included .1.3.6.1.2.1.25.1
                    ```
            2. 防火牆配置
               1. 關閉/允許特定網段接收
               2. 允許特定PORT連入
            3. 套用設定
                ```sh
                # 重新啟動 SNMP 服務
                sudo systemctl restart snmpd
                # 設定開機自動啟動
                sudo systemctl enable snmpd
                ```
      3. Librenms上加入Device測試

2. 全域設定
   1. 帳號
      1. 新增帳號
      2. 登入測試
      3. 刪除初始admin帳號
   2. 主題
      1. ⚙️ > Global Setting > Web UI > Style
      2. Dark
   3. 檢視設備方式
        > 預設看到設備名稱而非IP
      1. ⚙️ > Global Setting > Web UI > Device Setting
      2. sysName
3. 設備
   1. 加入設備add device
        ```sh
        # 進入container
        docker exec -it --user librenms librenms_web /bin/bash

        # 大量加入device
        #lnms device:add [yourhostname] [--v1|--v2c] [-c yourSNMPcommunity] 
        lnms device:add 192.168.1.2 --v2c -c HOME
        ```
   2. 查看資料拉取狀況
   3. 設備分組
      1. 後續用於告警規則...
4. 服務
   1. Add Service
      1. 設備
      2. 檢測方法
5. 設定告警
   1. 告警通路
      1. 通路測試
   2. 告警範本
   3. 告警規則
      1. rule
         1. 既有指標
            1. 停機告警(up/down)
            2. 域值告警(水線)
            3. 服務告警(服務Port)
         2. SQL
      2. 頻率控制
         1. 太頻繁呼叫API telegram會爆掉...
      3. 規則測試
         1. 調低告警域值，嘗試觸發訊息