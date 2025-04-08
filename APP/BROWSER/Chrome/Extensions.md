# Extensions

## SwitchyOmega socks5 proxy
1. 用ssh dynamic port forwarding 建立隧道
    > SSH遠端主機，並轉出代理到本機 9090 Port。
    ```powershell
    ssh -N -D 9090 #account#@#serverIP#
    ```
2. Proxy SwitchyOmega 設定
    1. chrome 安裝擴充元件Proxy SwitchyOmega
    2. 代理伺服器指向 localhost:9090
    * ![20220501144134](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220501144134.png)
    * ![20220501144213](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220501144213.png)
    3. 啟動代理
    * ![20220501144230](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220501144230.png)

3. 可以潛入#serverIP#能看到的網址了，看看平時關在防火牆內的網頁惹
    * ![20220501144947](https://raw.githubusercontent.com/orange9982239/ImageHosting/master/images/20220501144947.png)