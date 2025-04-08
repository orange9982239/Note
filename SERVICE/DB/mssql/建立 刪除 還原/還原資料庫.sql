--還原備份
USE [master]
	RESTORE DATABASE mydbname FROM DISK = 'D:\SHARE\mydbname_backup_2021_07_18_112310_0262915.bak' WITH REPLACE, NORECOVERY, move 'mydbname' to 'D:\mssql\mydbname.mdf', move 'mydbname_log' to 'D:\mssql\mydbname_log.ldf'
	RESTORE DATABASE mydbname FROM DISK = 'D:\SHARE\mydbname_backup_2021_07_19_060000_0129428.bak' WITH NORECOVERY
	RESTORE LOG mydbname FROM DISK = 'D:\SHARE\mydbname_backup_2021_07_19_060050_6265840.trn' WITH NORECOVERY
	RESTORE LOG mydbname FROM DISK = 'D:\SHARE\mydbname_backup_2021_07_19_070050_0659702.trn' WITH NORECOVERY
	RESTORE DATABASE mydbname WITH RECOVERY
GO