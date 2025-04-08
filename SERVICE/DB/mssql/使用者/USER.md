# USER


## 建立使用者
```sql
-- 定義變數
DECLARE @User       NVARCHAR(MAX) = N'{user}';

-- 建立動態 SQL
DECLARE @DynamicSQL NVARCHAR(MAX) = N'
USE [master]
--在master建立使用者
CREATE LOGIN ' + QUOTENAME(@User) + ' FROM WINDOWS WITH DEFAULT_DATABASE=[master]

--指派權限sysadmin
ALTER SERVER ROLE [sysadmin] ADD MEMBER ' + QUOTENAME(@User) + '
GO
';

SELECT @DynamicSQL;                                                 -- 查看動態 SQL
EXEC sp_executesql @DynamicSQL;                                     -- 執行動態 SQL

```

## 資料庫中加入使用者授權
```sql
-- 定義變數
DECLARE @Database   NVARCHAR(MAX) = N'{database_name}',
        @User       NVARCHAR(MAX) = N'{user}';

-- 建立動態 SQL
DECLARE @DynamicSQL NVARCHAR(MAX) = N'
USE ' + QUOTENAME(@Database) + '
CREATE USER ' + QUOTENAME(@User) + '
ALTER AUTHORIZATION ON SCHEMA::[db_owner] TO ' + QUOTENAME(@User) + '
ALTER ROLE [db_owner] ADD MEMBER ' + QUOTENAME(@User) + '
GO
';

SELECT @DynamicSQL;                                                 -- 查看動態 SQL
EXEC sp_executesql @DynamicSQL;                                     -- 執行動態 SQL
```


## 建立跨伺服器連結
```sql
USE [master]
GO
-- 宣告變數
DECLARE @Server         NVARCHAR(MAX) = N'{server_name}',           -- 連結伺服器名稱
        @TargetServerIP NVARCHAR(MAX) = N'{target_server_ip}',      -- 目標伺服器IP或主機名
        @Account        NVARCHAR(MAX) = N'{account}',               -- 遠端登入帳號
        @Password       NVARCHAR(MAX) = N'{password}',              -- 遠端登入密碼
        @TableName      NVARCHAR(MAX) = N'{tablename}';             -- 遠端資料表名稱(用於測試)

-- 建立連結伺服器
EXEC master.dbo.sp_addlinkedserver @server=@Server, @srvproduct=N'SQLNCLI', @provider=N'SQLNCLI11', @datasrc=N'#target_server_ip#'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'collation compatible', @optvalue=N'false'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'data access', @optvalue=N'true'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'dist', @optvalue=N'false'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'pub', @optvalue=N'false'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'rpc', @optvalue=N'false'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'rpc out', @optvalue=N'false'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'sub', @optvalue=N'false'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'connect timeout', @optvalue=N'0'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'collation name', @optvalue=null
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'lazy schema validation', @optvalue=N'false'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'query timeout', @optvalue=N'0'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'use remote collation', @optvalue=N'true'
EXEC master.dbo.sp_serveroption @server=@Server, @optname=N'remote proc transaction promotion', @optvalue=N'true'
EXEC master.dbo.sp_addlinkedsrvlogin @rmtsrvname=@Server, @locallogin=NULL , @useself=N'False', @rmtuser=@Account, @rmtpassword=@Password
GO

-- 測試跨伺服器連結
DECLARE @DynamicSQL NVARCHAR(MAX) = N'SELECT * FROM ' + QUOTENAME(@Server) + '.[dbo].' + QUOTENAME(@TableName);     -- 建立動態 SQL
SELECT @DynamicSQL;                                                                                                 -- 查看動態 SQL
EXEC sp_executesql @DynamicSQL;                                                                                     -- 執行動態 SQL
```