# mRemoteNG 

## 安裝
* https://mremoteng.org/

## Putty 改配色
1. 下載主題 https://github.com/AlexAkulov/putty-color-themes
   1. 找喜歡的配色https://github.com/AlexAkulov/putty-color-themes/blob/master/images/readme.md
   2. 下載reg
2. 登入reg
3. 測試顏色
    ```sh
    printf "          "
    for b in 0 1 2 3 4 5 6 7; do printf "  4${b}m "; done
    echo
    for f in "" 30 31 32 33 34 35 36 37; do
        for s in "" "1;"; do
            printf "%4sm" "${s}${f}"
            printf " \033[%sm%s\033[0m" "$s$f" "gYw "
            for b in 0 1 2 3 4 5 6 7; do
                printf " \033[4%s;%sm%s\033[0m" "$b" "$s$f" " gYw "
            done
            echo
        done
    done
    ```

## Filezilla 整合
* 顯示名稱
  * SFTP
* 檔案名稱
  * filezilla.exe的路徑
  * D:\0.software\2.portable\FileZilla-3.66.4\filezilla.exe
* 引數
  * sftp://%Username%:%Password%@%Hostname%:22%Userfield%
  * [若連間異常Password改!Password]sftp://%Username%:%!Password%@%Hostname%:22%Userfield% 
* V
  * 合整試嘗

## 大量編輯xml
1. 拉資料夾，製作`連線範本`
2. 匯出XML
3. vscode編輯XML
   1. 透過`EXCEL公式`將`IP表`帶入`連線範本`
      1. name(server name + ip尾碼)
      2. ip
      3. uuid
   2. 回寫xml
4. 匯入XML