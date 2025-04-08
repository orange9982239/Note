# SQL SERVER 繼承舊帳號


> * 帳號是在`SQL SQRVER伺服器上`的
> * user 是在`資料庫內`的

> * 用備份檔案還原資料庫到全新DB時，就變成`有資料庫使用者，沒帳號的情況`
> 1. 從還原的資料庫(#db_name#)取出sid(#SID#)
> 2. SQL SQRVER伺服器建立同名的user(#db_user_name#)，並同時給定sid(#SID#)

``` sql
--取得前資料庫的sid -- 0x5AE9495ATTTTTTTTTT49E082877EC25A
SELECT sid FROM #db_name#.sys.sysusers WHERE name='#db_user_name#';

--建立#db_user_name#登入帳號並直接給定前資料庫sid
USE [master]
    CREATE LOGIN [#db_user_name#] WITH PASSWORD=N'#db_password#', 
    DEFAULT_DATABASE=[master],
    CHECK_EXPIRATION=OFF, 
    CHECK_POLICY=OFF,
    SID = #SID#--0x5AE9495ATTTTTTTTTT49E082877EC25A
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [#db_user_name#]
GO

--ref https://blog.miniasp.com/post/2007/11/18/SQL-Backup-and-Restore-cause-ASPNET-Can-not-Login
```