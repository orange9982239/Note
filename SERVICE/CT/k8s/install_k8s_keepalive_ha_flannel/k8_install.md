# install_k8s_keepalive_ha_flannel
1. Kubeadm VM配置
    | hostname      | IP           | system           | memory | k8s-version |
    | ------------- | ------------ | ---------------- | ------ | ----------- |
    | k8s_vip       | 192.168.0.40 | -                | -      | v1.30.13    |
    | k8s-master-01 | 192.168.0.41 | Ubuntu 24.04 LTS | 4GB    | v1.30.13    |
    | k8s-master-02 | 192.168.0.42 | Ubuntu 24.04 LTS | 4GB    | v1.30.13    |
    | k8s-master-03 | 192.168.0.43 | Ubuntu 24.04 LTS | 4GB    | v1.30.13    |
    | k8s-worker-01 | 192.168.0.44 | Ubuntu 24.04 LTS | 2GB    | v1.30.13    |
    | k8s-worker-02 | 192.168.0.45 | Ubuntu 24.04 LTS | 2GB    | v1.30.13    |
2. 溝通圖
    ```mermaid
    graph TD
        subgraph MASTER
            MASTER1[k8s-master-01<br>192.168.0.41<br>4GB]
            MASTER2[k8s-master-02<br>192.168.0.42<br>4GB]
            MASTER3[k8s-master-03<br>192.168.0.43<br>4GB]
        end

        subgraph WORKER
            WORKER1[k8s-worker-01<br>192.168.0.44<br>2GB]
            WORKER2[k8s-worker-02<br>192.168.0.45<br>2GB]
        end

        %% MASTER中一節點持有VIP
        VIP[k8s_vip<br>192.168.0.40]
        VIP <-. 持有VIP<br>受到VIP MASTER控制 .-> MASTER1
        VIP <-. 持有VIP<br>受到VIP MASTER控制 .-> MASTER2
        VIP <-. 持有VIP<br>受到VIP MASTER控制 .-> MASTER3

        VIP -. 受到VIP MASTER控制 .-> WORKER1
        VIP -. 受到VIP MASTER控制 .-> WORKER2
    ```
    1. 給個MASTER節點都可能成為控制集群的Leader
       1. 由`持有VIP的MASTER節點`控制集群
    2. 每一台WORKER都受到`持有VIP的MASTER節點`控制
3. 安裝kubeadm
   1. 防止ubuntu24 cloud init改ip
       ```sh
       echo 'network: {config: disabled}' | sudo tee /etc/cloud/cloud.cfg.d/90-installer-network.cfg > /dev/null
       ```
   2. 安裝前配置腳本
      ```sh
      curl -fsSL https://raw.githubusercontent.com/xiaopeng163/learn-k8s-from-scratch/master/source/_code/k8s-install/install.sh -o install.sh

      sudo sh install.sh
      ```
   3. kubeadm指定版本並安裝
      ```sh
      # 會列出可安裝kubeadm版本
      sudo apt list -a kubeadm
      
      # 自行選擇要的版本
      VERSION=1.30.13-1.1
      sudo apt install -y kubeadm=$VERSION kubelet=$VERSION kubectl=$VERSION

      # 卡住版本
      ## sudo apt-mark hold kubelet kubeadm kubectl
      ## sudo apt-mark unhold kubelet kubeadm kubectl

      # 確認安裝版本
      kubeadm version
      kubelet --version
      kubectl version --client=true

      # 拉取集群所需要的images
      sudo kubeadm config images pull
      ```
   4. 製作VM TEMPLET
4. MASTER節點
   1. MASTER1初始化
      1. 改IP及hostname名稱
          ```sh
          sudo su
          vim /etc/netplan/50-cloud-init.yaml
          vim /etc/hostname
          vim /etc/hosts

          # 重啟套用變更
          reboot
          ```
      2. 配置VIP
          ```sh
          # 安裝 Keepalived
          sudo apt-get update
          sudo apt-get install -y keepalived

          # 健康檢查腳本
          sudo vim /etc/keepalived/check_apiserver.sh
          sudo chmod +x /etc/keepalived/check_apiserver.sh

          # 配置 Keepalived
          sudo vim /etc/keepalived/keepalived.conf

          # 啟動並驗證 Keepalived
          sudo systemctl start keepalived
          sudo systemctl enable keepalived
          sudo systemctl status keepalived # 確認服務是否正常運行

          # 綁定檢查
          ip a | grep "vip"
          ```
      3. 初始化kubeadm
          ```sh
          # 開始初始化
          ## --apiserver-advertise-address    这个地址是本地用于和其他节点通信的IP地址，衝常綁VIP
          ## --pod-network-cidr               pod network 地址空间
          sudo kubeadm init \
              --control-plane-endpoint="192.168.0.40:6443" \
              --upload-certs \
              --pod-network-cidr=10.244.0.0/16
          ```
      4. 記錄輸出的 `kubeadm join` 命令**（含 Token 和 Cert Hash）
   2. MASTER2,MASTER3加入
      * 修正名稱
        ```sh
        vim /etc/hostname
        vim /etc/hosts

        # 重啟套用變更
        reboot
        ```
      * 配置VIP
        ```sh
        # 安裝 Keepalived
        sudo apt-get update
        sudo apt-get install -y keepalived

        # 健康檢查腳本
        sudo vim /etc/keepalived/check_apiserver.sh
        sudo chmod +x /etc/keepalived/check_apiserver.sh

        # 配置 Keepalived
        sudo vim /etc/keepalived/keepalived.conf

        # 啟動並驗證 Keepalived
        sudo systemctl start keepalived
        sudo systemctl enable keepalived
        sudo systemctl status keepalived # 確認服務是否正常運行

        # 綁定檢查
        ip a | grep "192.168.0.40"
        ```
      * JOIN指令
        ```sh
        # kubeadm join 192.168.0.40:6443 \
        #     --token <token> \
        #     --discovery-token-ca-cert-hash <hash> \
        #     --control-plane \
        #     --certificate-key <cert-key>

        kubeadm join 192.168.0.40:6443 \
            --token rwg9fg.0uapsx3t22stvbn7  \
            --discovery-token-ca-cert-hash sha256:6bece176fab5fc524fd21e237c69fc3c976285962d252361f7b6a4afd6176ea2 \
            --control-plane \
            --certificate-key a20b5f67a3c97cb349306f4d4279a225df8410ec8ae04177e2cbaf6b5fb03d3f
        ```
      * 若你太慢加須回到k8s-master-01上重新產生
        ```
        # token
        kubeadm token create

        # hash
        openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | \
        openssl dgst -sha256 -hex | sed 's/^.* //'

        # cert-key
        sudo kubeadm init phase upload-certs --upload-certs
        ```
   3. 準備 .kube
        ```sh
        # 配置
        mkdir -p $HOME/.kube
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        sudo chown $(id -u):$(id -g) $HOME/.kube/config
        
        # 測試cluster
        kubectl get nodes
        kubectl get pods -A

        # Bash source 
        source <(kubectl completion bash)
        echo "source <(kubectl completion bash)" >> ~/.bashrc
        ```
   4. 部署pod network方案CNI
      1. 本次選擇flannel
      2. 設定檔案
          ```
          # 取得
          curl -LO https://raw.githubusercontent.com/flannel-io/flannel/v0.24.2/Documentation/kube-flannel.yml

          # 調整設定檔案
          sudo vim kube-flannel.yml
          ## 設定POD的網路CIDR        
          ### net-conf.json: |
          ###     {
          ###         "Network": "10.244.0.0/16",
          ###         "Backend": {
          ###             "Type": "vxlan"
          ###         }
          ###     }
          ## 設定網卡名稱 => eth0
          ###     args:
          ###     - --ip-masq
          ###     - --kube-subnet-mgr
          ###     - --iface=eth0                              # 加入這行指向自己的網卡
           
          # 套用網路設定
          ## 改名
          mv kube-flannel.yml flannel.yaml
          ## 套用
          kubectl apply -f flannel.yaml
          ```
      3. 測試cluster
          ```sh
          # 測試cluster
          kubectl get nodes
          ## 此時STATUS會出現Ready代表成功
          ## NAME            STATUS   ROLES           AGE    VERSION
          ## k8s-master-01   Ready    control-plane   147m   v1.30.13
          ## k8s-master-02   Ready    control-plane   37m    v1.30.13
          ## k8s-master-03   Ready    control-plane   74m    v1.30.13
          ```
5. WORKER節點
   1. 改IP及hostname名稱
      ```sh
      sudo su
      vim /etc/netplan/50-cloud-init.yaml
      vim /etc/hostname
      vim /etc/hosts

      # 重啟套用變更
      reboot
      ```
   2. WORKER1,WORKER2節點加入
      ```sh
      sudo su
      
      # kubeadm join 192.168.0.40:6443 \
      #     --token <token> \
      #     --discovery-token-ca-cert-hash <hash>

      kubeadm join 192.168.0.40:6443 \
          --token rwg9fg.0uapsx3t22stvbn7  \
          --discovery-token-ca-cert-hash sha256:6bece176fab5fc524fd21e237c69fc3c976285962d252361f7b6a4afd6176ea2
      ```
6. 測試cluster
   1. 回到master節點
   2. 測試cluster
      > 由3台master節點構成的k8s_cluster可容忍1節點故障
      ```sh
      kubectl get nodes
      ## NAME            STATUS   ROLES           AGE    VERSION
      ## k8s-master-01   Ready    control-plane   130m   v1.30.13
      ## k8s-master-02   Ready    control-plane   19m    v1.30.13
      ## k8s-master-03   Ready    control-plane   57m    v1.30.13
      ## k8s-worker-01   Ready    <none>          9m9s   v1.30.13
      ## k8s-worker-02   Ready    <none>          67s    v1.30.13

      kubectl get pods -A
      ## NAMESPACE      NAME                                    READY   STATUS    RESTARTS       AGE
      ## kube-flannel   kube-flannel-ds-7jsjt                   1/1     Running   0              10m
      ## kube-flannel   kube-flannel-ds-bd8jb                   1/1     Running   0              27m
      ## kube-flannel   kube-flannel-ds-mtrbz                   1/1     Running   0              2m25s
      ## kube-flannel   kube-flannel-ds-tbwff                   1/1     Running   0              27m
      ## kube-flannel   kube-flannel-ds-wzb6x                   1/1     Running   0              21m
      ## kube-system    coredns-55cb58b774-jjb67                1/1     Running   0              131m
      ## kube-system    coredns-55cb58b774-rcd4j                1/1     Running   0              131m
      ## kube-system    etcd-k8s-master-01                      1/1     Running   10             131m
      ## kube-system    etcd-k8s-master-02                      1/1     Running   0              21m
      ## kube-system    etcd-k8s-master-03                      1/1     Running   0              58m
      ## kube-system    kube-apiserver-k8s-master-01            1/1     Running   9              131m
      ## kube-system    kube-apiserver-k8s-master-02            1/1     Running   1              21m
      ## kube-system    kube-apiserver-k8s-master-03            1/1     Running   0              58m
      ## kube-system    kube-controller-manager-k8s-master-01   1/1     Running   10 (67m ago)   131m
      ## kube-system    kube-controller-manager-k8s-master-02   1/1     Running   1              21m
      ## kube-system    kube-controller-manager-k8s-master-03   1/1     Running   0              58m
      ## kube-system    kube-proxy-2qpwk                        1/1     Running   0              10m
      ## kube-system    kube-proxy-h95pz                        1/1     Running   0              58m
      ## kube-system    kube-proxy-k9p5z                        1/1     Running   0              131m
      ## kube-system    kube-proxy-x5vjm                        1/1     Running   0              2m25s
      ## kube-system    kube-proxy-z9lnn                        1/1     Running   0              21m
      ## kube-system    kube-scheduler-k8s-master-01            1/1     Running   10 (67m ago)   131m
      ## kube-system    kube-scheduler-k8s-master-02            1/1     Running   1              21m
      ## kube-system    kube-scheduler-k8s-master-03            1/1     Running   0              58m
      ```