# build
1. 準備
   1. Visual Studio Build Tools 2019
        ```ps1
        # 安裝2019.BuildTools=>這邊會順便自動安裝Visual Studio Installer
        winget install --id=Microsoft.VisualStudio.2019.BuildTools  -e
        
        # Visual Studio Installer內安裝[C++桌面開發](超級慢)

        # 加入系統PATH
        C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\Hostx86\x64
        
        # 驗證
        cl
        ## Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30158 for x64
        ## Copyright (C) Microsoft Corporation.  著作權所有，並保留一切權利。
        ## 使用方式: cl [ option... ] filename... [ /link linkoption... ]
        ```
   2. miniconda
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
   3. git下載專案
        ```ps1
        git clone https://github.com/NVlabs/stylegan2-ada-pytorch
        ```
   4. 建立文字檔案environment.yml
        ```yml
        name: stylegan2-ada
        channels:
          - pytorch
          - nvidia
          - conda-forge
          - defaults
        dependencies:
          - python=3.7
          - pip
          - numpy
          - pip:
            - click
            - requests
            - tqdm
            - pyspng
            - ninja
            - imageio-ffmpeg==0.4.3
            - imageio
            - psutil
            - tensorboard
            - pillow==8.4.0
        ```
2. 用conda建置
    > 網路有點慢要等等
    ```ps1
    # 根據environment.yml建置conda環境
    conda env create -f environment.yml
    
    # 進入stylegan2-ada環境
    conda activate stylegan2-ada

    # 補上conda安裝pytorch
    conda install pytorch=1.7.1 torchvision=0.8.2 torchaudio=0.7.2 cudatoolkit=11.0 -c pytorch

    # 補上pip安裝pillow
    pip install pillow==8.4.0
    ```
3. 官方測試產圖
    ```ps1
    python generate.py --outdir=out --trunc=1 --seeds=85,265,297,849 --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/metfaces.pkl
    python generate.py --outdir=out --trunc=0.7 --seeds=600-605 --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/metfaces.pkl
    ```
4. 執行
   1. 資料集打包
    ```ps1
    # 還沒開始
    python dataset_tool.py --source=D:\reserch\preImage\star_crack --dest=D:\reserch\stylegan_dataset\star_crack_dataset.zip
    ```
   2. 訓練
    > 產出模型pki檔案
    ```ps1
    # 訓練
    python train.py  --outdir=D:\reserch\outtest_ada  --data=D:\reserch\stylegan_dataset\black_core0319_100peice_ffhq256x256.zip --cfg=paper256 --batch=16 --kimg=3000 --gamma=10 --aug=ada  --gpus=1 --snap=10

    # 繼續訓練
    python train.py  --outdir=D:\reserch\outtest_ada  --data=D:\reserch\stylegan_dataset\black_core0319_100peice_ffhq256x256.zip --cfg=paper256 --batch=16 --kimg=360 --gamma=10 --aug=ada  --gpus=1 --snap=10 --resume=D:\reserch\outtest_ada\00003-black_core0319_100peice_ffhq256x256-paper256-gamma10-kimg3000-batch16-ada\network-snapshot-002640.pkl
    ```
   3. 產圖
    ```ps1
    # 還沒開始
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