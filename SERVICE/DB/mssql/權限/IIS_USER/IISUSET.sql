USE [master]
    --創建帳號
    CREATE LOGIN [IIS APPPOOL\#iisUserName#] FROM WINDOWS;
GO

USE [#mydatabase#]
    --創建使用者
    CREATE USER [IIS APPPOOL\#iisUserName#] FOR LOGIN [IIS APPPOOL\#iisUserName#]

    --使用者增加權限
    ALTER ROLE [db_owner] ADD MEMBER [IIS APPPOOL\#iisUserName#]
GO