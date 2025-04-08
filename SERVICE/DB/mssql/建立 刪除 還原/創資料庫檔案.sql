--創資料庫檔案
USE [master]
	CREATE DATABASE
		mydbname
	ON PRIMARY (
		NAME=mydbname,
		FILENAME = 'D:\MSSQL\mydbname.mdf'
	)
	LOG ON (
		NAME=mydbname_log,
		FILENAME = 'D:\MSSQL\mydbname_log.ldf'
	)
GO
