# PVE 備份還原
> https://pve.proxmox.com/wiki/Backup_and_Restore
## 備份
    
1. 指定虛擬機 > 備份頁籤 > 立即備份
    > ![20220727151445](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220727151445.png)


2. 備份
    > ![20220727151808](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220727151808.png)
   
## 還原
1. local(PVE) > 備份 > 指定檔案 > 還原
    > ![20220727152426](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220727152426.png)
2. 儲存     => 要將VM資料存在哪個硬碟
   VM ID    => 填入不存在的VM代表進行`異機還原`，會自動建立VM
   頻寬限制 => 限速用，以免拖垮效能。
   唯一     => 勾選可避免複製VM時會出現uuid或mac衝突。
   > ![20220727152635](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220727152635.png)

## 取出備份檔案
1. vm預設備份路徑
    ```bash
    cd /var/lib/vz/dump/
    ```
2. scp 跨VM複製備份檔案
    ```bash
    # 登入PVE Server 192.168.1.2 
    ssh root@192.168.1.2

    # SCP複製備份檔案192.168.1.1複製至192.168.1.2
    # 檔案路徑/var/lib/vz/dump/vzdump-qemu-101-2022_07_26-15_26_47.vma.zst
    scp root@10.1.111.1:/var/lib/vz/dump/vzdump-qemu-101-2022_07_26-15_26_47.vma.zst /var/lib/vz/dump/vzdump-qemu-101-2022_07_26-15_26_47.vma.zst
    ```
# PVE 防火牆設定
## 一、資料中心防火牆
> 先設定好`允許管理的群組`，再開防火牆，以免鎖死自己。
1. IPSET => 設定好IPSET群組
    > 建立全組加入機器IP，後續用於管理權限較方便。
    ![20220430163300](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220430163300.png)
    * 人的群組
	    1. 管理者(網管)
        2. 使用者(開發者)
    * 機器的群組
        1. PVE_WEBUI
	    2. 虛擬機們

2. 設定防火牆規則
![20220430164516](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220430164516.png)
    1. 允許 SSH
    * ![20220430165055](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220430165055.png)
    2. 允許 TCP 8006(PVE web管理介面)
    * ![20220430165419](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220430165419.png)
3. 防火牆開起來
* ![20220430165730](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220430165730.png)
## 二、節點防火牆
1. 防火牆開起來

## 三、啟用客體機防火牆
1. 設定防火牆規則
    1. 管理者(網管)
        * SSH
        * RDP
        * MSSQL
    2. 使用者(開發者)
        * MSSQL
2. 防火牆開起來