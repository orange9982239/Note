# Cygwin
* 核心功能：在 Windows 上模擬 Linux 環境。
* 適用對象：熟悉 Linux 的使用者、跨平台開發者、希望學習 Linux 的 Windows 使用者。
* 用途：執行 Linux 指令、開發和編譯 Linux 程式、模擬 POSIX API。

## 安裝
```ps1
winget install --id=Cygwin.Cygwin  -e
# 安裝常用工具
## * 文字編輯
##   * vim
##   * nano
## * cli browser
##   * wget
##   * curl
##   * openssl
## * ssh
##   * openssh
##   * cygrunsrv
##   * autossh
## * 同步
##   * rsync
## * 加密
##   * gnupg2
```

## cygrunsrv (SSH server)
> 讓windows上有ssh server的功能，不過建議改用openssh
### 安裝
1. 設定cygrunsrv
    * 以管理員權限執行cygwin
    * cygwin bash
        ```bash
        ssh-host-config -y
        ```
2. 啟動服務=>`CYGWIN cygsshd`  
3. 防火牆允許22 Port
4. ssh連線測試

### Home Directory match Windows Home Directory
> 讓cygwin的home目錄與windows的home目錄相同
1. 編輯 設定檔案
    ```bash
    vim /etc/nsswitch.conf
    ```
2. 將 `# db_home:  /home/%U`改成`# db_home:  /%H`
3. 重啟cygwin，使用`pwd`命令檢查home目錄是否由`/home/<<user>>`變成`/cygdrive/c/Users/<<user>>`