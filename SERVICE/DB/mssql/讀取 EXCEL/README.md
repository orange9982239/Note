# Mssql Read Excel

## 啟動
1. 安裝AccessDatabaseEngine_X64
2. sp_configure
    ```sql
    sp_configure 'show advanced options', 1;
    RECONFIGURE;  --Added        
    sp_configure 'Ad Hoc Distributed Queries', 1;
    RECONFIGURE;
    ```
3. 給Microsoft.ACE.OLEDB.12.0權限
    ```sql
    USE [master]
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'AllowInProcess', 1
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'DisallowAdHocAccess', 1
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'DynamicParameters', 1
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'IndexAsAccessPath', 1
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'LevelZeroOnly', 1
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'NestedQueries', 1
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'NonTransactedUpdates', 1
        EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'SqlServerLIKE', 1
    GO
    ```
4. `servic.msc`設定啟動 user
    * ![20220308214348](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220308214348.png)
5. 登入頁簽 ⇒ 本機使用者帳戶
    * ![20220308214410](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220308214410.png)
6. 重啟服務服務
    * ![20220308214434](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220308214434.png)

## 測試
1. 建立假資料
   1. 在`C:\tmp`建立test.xlsx
    * ![20220308214549](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220308214549.png)
   2. 加入假資料
    * ![20220308214605](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220308214605.png)
2. 讀取
    > 無法初始化連結伺服器 "(null)" 的 OLE DB 提供者 "Microsoft.ACE.OLEDB.12.0" 的資料來源物件。

    > 這個錯誤代表你開著那個EXCEL檔案。

    ```sql
    SELECT * 
    FROM OPENROWSET(
        'Microsoft.ACE.OLEDB.12.0',
        'Excel 12.0 Xml;Database=C:\tmp\test.xlsx;', 
        'SELECT * FROM [工作表1$A1:C3]'
    );

    -- 只能讀全部無法控制range
    -- SELECT * FROM
    -- OPENDATASOURCE (
    --     'Microsoft.ACE.OLEDB.12.0',
    --     'Excel 12.0;HDR=Yes;IMEX=1;Database=C:\Users\orange9982239\Desktop\test.xlsx'
    -- )... [工作表1$]
    ```

    * ![20220308214748](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220308214748.png)