--刪除資料庫檔案(包含 mdf ldf)
USE [master];
	EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'mydbname'
	ALTER DATABASE [mydbname] SET  SINGLE_USER WITH ROLLBACK IMMEDIATE
	DROP DATABASE [mydbname]
GO