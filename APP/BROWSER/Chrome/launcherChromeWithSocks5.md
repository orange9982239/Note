# launcherChromeWithSocks5

## 功能
> 讓google瀏覽器能直接透過ssh隧道建立的socks5代理連接內網的網頁。

## 準備
1. ssh client
2. chrome

## 操作
1. 透過ssh建立socks5代理
    ```ps1
    ssh -D 127.0.0.1:9090 lmadmin@10.100.70.237
    ```
2. 透過CLI啟動chrome並連接代理伺服器
    ```ps1
    # cd到chrome路徑
    cd "C:\Program Files (x86)\Google\Chrome\Application"

    # 透過CLI啟動chrome並連接代理伺服器
    .\chrome.exe --proxy-server="socks5://127.0.0.1:9090" --host-resolver-rules="MAP * 0.0.0.0 , EXCLUDE 127.0.0.1" --user-data-dir="%TEMP%\ChromeProfile"
    ```