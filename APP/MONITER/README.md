# MONITER
## 1. 收集資料
### 1.1 os層級
* snmp
* agent
### 1.2 bmc層級
* syslog
* snmp trap

## 2. 儲存資料
### 2.1 時序資料庫
### 2.2 一般DB

## 3. 資料處理
> 作為告警指標
### 3.1 資料庫資料
### 3.2 資料庫計算指
> 從資料庫資料計算平均硬碟用量
### 3.3 LOG類型資料萃取
> bmc層級syslog中用regexp萃取事件字串

## 4. 告警
> 注意要設計可開關告警
### 4.1 停機告警(up/down)
### 4.2 域值告警(水線)
### 4.3 服務告警(服務Port)
### 4.4 自訂義告警(腳本告警)
### 4.5 硬體告警(收集來自BMC送入的log資料)