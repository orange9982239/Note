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
  * SFTP
    * 顯示名稱
      * WinSCP_SFTP
    * 檔案名稱
      * WinSCP的路徑
      * %USERPROFILE%\AppData\Local\Programs\WinSCP\WinSCP.exe
    * 引數
      > 若連間異常!Password改Password
      * sftp://%Username%:%!Password%@%Hostname%:%Port%
    * 選項V
      * 等待結束
  * FTP
    * 顯示名稱
      * WinSCP_FTP
    * 檔案名稱
      * WinSCP的路徑
      * %USERPROFILE%\AppData\Local\Programs\WinSCP\WinSCP.exe
    * 引數
      > 若連間異常!Password改Password
      * ftp://%Username%:%!Password%@%Hostname%:%Port%
    * 選項V
      * 等待結束

## Edge 整合
  * HTTP
    * 顯示名稱
      * Edge_http
    * 檔案名稱
      * C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
    * 引數
      * --inprivate http://%Hostname%:%Port%
  * Edge_https
    * 顯示名稱
      * Edge_http
    * 檔案名稱
      * C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
    * 引數
      * --inprivate https://%Hostname%:%Port%

## Puppteer+Edge 整合
1. puppteer安裝
  ```ps1
  winget install OpenJS.NodeJS.LTS
  npm install puppeteer-core
  ```
1. js腳本
  > C:\tmp\mRemoteNG-puppteer-edge-https-login.js
  ```js
  const puppeteer = require('puppeteer-core');

  // 取得命令列參數
  let [,, url, username, password] = process.argv;

  (async () => {
    const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

    const browser = await puppeteer.launch({
      executablePath: edgePath,
      headless: false,
      args: ['--inprivate', '--start-maximized']
    });

    // 取得第一個 incognito context 並在其中開新頁面
    const context = browser.defaultBrowserContext();
    const pages = await browser.pages();
    const page = pages.length > 0 ? pages[0] : await browser.newPage();

    // 設定視窗大小為全螢幕
    await page.setViewport();
    // 關閉js alert視窗
    page.on('dialog', async dialog => {
      console.log('Dialog message:', dialog.message());
      await dialog.accept();
    });
    await page.goto(url);

    try {
      switch (true) {
        case url.includes('your-website.com'):
          // 根據網站的登入表單結構填寫
          await page.type('input[id="Login1_UserName"]', username);
          await page.type('input[id="Login1_Password"]', password);
          await page.click('#Login1_LoginButton');
          break;
        default:
          break;
      }
      await page.waitForNavigation();
    } catch (error) {
      console.log(error);
      console.error('無法找到登入表單，請檢查網址或手動登入。');
      // 登入後自動關閉
      // await browser.close();                                 
      return;
    }
  })();
  ```
1. 外部工具
  * puppteer-edge-http
    node
    C:\tmp\mRemoteNG-puppteer-edge-https-login.js "http://%Hostname%:%Port%" "%Username%" "%!Password%"
  * puppteer-edge-https
    node
    C:\tmp\mRemoteNG-puppteer-edge-https-login.js "https://%Hostname%" "%Username%" "%!Password%"

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