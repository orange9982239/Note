# SSHFS-Win

## 功能
> mount sftp 到windows上類似於SMB但比較安全(走ssh協議)

> 用於SSMS資料庫還原，可直接讀取備份檔案。

* 經測試
    - [ ] ✔️用於SSMS資料庫還原。
    - [ ] ❌iso檔案無法成功mount
    - [ ] ❌某些資料夾內容無法讀取，原因不明。
      * ![20220309170011](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220309170011.png)
## 準備
> [winfsp官網](https://winfsp.dev/rel/) 下載兩個項目
 - [x] SSHFS-Win (x64) 
 - [x] WinFsp

## 設定
1. 安裝好`WinFsp`、`SSHFS-Win (x64)`
2. 檔案總管連線網路磁碟機
   * ![20220309160827](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220309160827.png)
3. 編輯mount路徑
    * ![20220309155513](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220309155513.png)
    1. 選擇磁碟機代號
    2. 資料夾 `\\sshfs\#account#@192.168.1.1`
       * 補充 => 若port不是在22，請更改名稱資料夾路徑`\\sshfs\#account#@192.168.1.1`
    3. 完成。 
4. 輸入帳密並登入。
    * ![20220309160923](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220309160923.png)
5. 效果如同SMB連線。
    * ![20220309155613](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220309155613.png)

## 中斷連線
> 保持良好資安習慣，不需要使用時，在該網路磁碟機上按`右鍵`>`中斷`。
* ![20220309161540](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220309161540.png)

## SSMS 讀取效果
* > 直接指定mount的網路磁碟路徑即可。
![20220309160155](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220309160155.png)

## REF
1. https://yowlab.idv.tw/wordpress/?p=99
2. https://github.com/winfsp/sshfs-win/issues/92