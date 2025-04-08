# HyperV虛擬交換機


## 內部網路 set IP
1. hyperv 虛擬交換機

2. 更改虛擬交換機`內部網路`在Host OS中網卡的設定
  1. 找hyperv 虛擬交換機建立的虛擬網卡
  * ![20211211214439](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20211211214439.png)
  2. `內容` > `IPV4` > `手動設定IP&Mask`
  * ![20211211214715](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20211211214715.png) 

3. VM Ubuntu 內部設定
    > * 虛擬交換機`外部網路`對應`eth0網卡`
    > * 虛擬交換機`內部網路`對應`eth1網卡` 

  1. 修改netplan
      > sudo vim /etc/netplan/00-installer-config.yaml
      
      * <kbd>i</kbd> 編輯
      * 輸入內容
        ``` yaml
        network:
          ethernets:
            eth0:
              dhcp4: true
            eth1:
              addresses: [192.168.1.11/24]
              nameservers:
                addresses: [192.168.1.1]
              dhcp4: false
          version: 2
        ```
      * <kbd>esc</kbd> 離開編輯
      * 輸入 `:wq` 儲存並關閉
      * 檢查成功與否
        ``` sh
        cat /etc/netplan/00-installer-config.yaml
        ```
  2. 執行netplan
      > sudo netplan apply
  3. 從Host os 測試IP設定是否成功
      > ssh root@192.168.1.11 
* ref
  * https://www.cnblogs.com/kasnti/p/11727755.html