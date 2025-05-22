# build
1. 準備
   1. miniconda
      ```ps1
      # 安裝
      winget install -e --id Anaconda.Miniconda3
      # 管理員權限下允許powershell
      set-executionpolicy remotesigned
      
      # 手動加入USER PATH
      ## %USERPROFILE%\miniconda3\condabin
      $env:path

      # powershell整合
      conda init powershell
      conda config --set auto_activate_base false

      # 驗證
      conda
      ```
   2. git clone
      ```ps1
      # cd到自己存放github的路徑
      cd ~\Documents\github.com\
      # clone labelImg專案
      git clone https://github.com/tzutalin/labelImg.git
      cd labelImg
      ```
   3. 用conda建置labelImg環境
      ```ps1
      # 建立python3.12環境，取名labelImg
      conda create -n labelImg python=3.12 -y
      # 進入環境
      conda activate labelImg

      # 補安裝依賴
      pip install PyQt5 lxml
      pyrcc5 -o libs/resources.py resources.qrc
      ```
   4. labelimg
      1. 類別文件
         1. 範例類別文件`%USERPROFILE%\Documents\github.com\labelImg\data\predefined_classes.txt`
         2. 製作`自訂類別檔案`
            1. 建立txt檔案`%USERPROFILE%\Documents\github.com\labelImg\data\my_classes.txt`
            2. 輸入類別後儲存
      2. 啟動
         ```ps1
         ## 帶參數啟動 python labelImg.py [圖片目錄路徑] [類別文件路徑] [保存目錄路徑]
         python labelImg.py "D:\reserch\preImage\crack" "%USERPROFILE%\Documents\github.com\labelImg\data\my_classes.txt" "D:\test\"

         ## 儲存格式按到變成YOLO

         ##[保存目錄路徑]無法帶入，需要自行用GUI按才能帶入
         ### 1. 改變目錄
         ### 2. 重新選擇[保存目錄路徑]=>"D:\test"
         ```
      3. 標記
         1. 左下角`創建區塊`
         2. 選取圖片中位置
         3. 選擇標籤類別
            1. 按OK
            2. 出現在右上方
         4. 存標記檔案
            1. 按CTRL+S
            2. LOG會顯示已存放至[保存目錄路徑]並列出標記檔案路徑
                ```log
                Image:D:\reserch\preImage\crack\img000002.jpg -> Annotation:D:/test\img000002.txt
                ```


# conda操作
```ps1
# 查詢conda下有多少個虛擬環境
conda env list

# 啟用虛擬環境
conda activate {ENVIRONMENT}    # stylegan3,base

# 停用虛擬環境
conda deactivate

# 編輯完yml檔案後更新環境
conda env update --name {ENVIRONMENT} --file environment.yml --prune

# 刪除虛擬環境
conda remove --name {ENVIRONMENT} --all

# 察看環境下的包
conda list -n {ENVIRONMENT}
```