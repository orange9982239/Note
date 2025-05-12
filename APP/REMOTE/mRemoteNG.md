# mRemoteNG 

## 安裝
* https://mremoteng.org/

## Putty 美化
1. 改配色
	1. 下載配色檔案
		1. 參考https://github.com/AlexAkulov/putty-color-themes/blob/master/images/readme.md
            > * 推薦
            > * `28. Monokai Dimmed.reg`
		2. 下載REG 
	2. 登入REG
	3. 改配色需要`關掉整個mRemoteng後打開`才能套用到putty
2. 改字
	1. 讀取設定
		1. 工具 > 選項
		2. 進階 > 啟動PuTTY
		3. Session > Default Setting > Load
	2. 編輯字體及大小
		* Windows > Apperance > Font Settings > Change...
          > - 推薦配置 
          >   * Cascadia Mono 
          >   * 14
	3. 儲存設定
		* Session > Default Setting > Save
3. 測試顏色
   > 開個帶有bash的ssh連線做測試
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
1. 安裝`Filezilla`
    > 官網下載安裝
2. mRemoteNG外部工具整合
  * 顯示名稱
    * FILEZILLA_SFTP
  * 檔案名稱
    * filezilla.exe的路徑
    * D:\0.software\2.portable\FileZilla-3.66.4\filezilla.exe
  * 引數
    > 若連間異常Password改!Password
    * sftp://%Username%:%Password%@%Hostname%:22%Userfield%
  * 合整試嘗
    * V

## WinSCP 整合
1. 安裝`WinSCP`
    ```ps1
    winget install -e --id WinSCP.WinSCP
    ```
2. mRemoteNG外部工具整合
  * 顯示名稱
    * WinSCP_SFTP
  * 檔案名稱
    * WinSCP的路徑
    * %USERPROFILE%\AppData\Local\Programs\WinSCP\WinSCP.exe
  * 引數
    > 若連間異常!Password改Password
    * sftp://%Username%:%!Password%@%Hostname%:%Port%
  * 合整試嘗
    * V

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