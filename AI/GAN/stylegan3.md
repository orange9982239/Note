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
   3. environment.yml下channels區塊改成
        ```yml
        channels:
        - pytorch
        - nvidia
        - conda-forge
        - defaults
        ```
2. 用conda建置
    > 網路有點慢要等等
    ```ps1
    # 根據environment.yml建置conda環境
    conda env create -f environment.yml
    
    # 進入stylegan3環境
    conda activate stylegan3

    # 補setuptools
    pip install setuptools==59.5.0
    
    # nvcc安裝(超級慢)
    conda install -c conda-forge cudatoolkit-dev -y

    # nvcc驗證
    nvcc --version
    ```
3. 官方測試產圖
    ```ps1
    python gen_images.py --outdir=out --trunc=1 --seeds=2 --network=https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-afhqv2-512x512.pkl

    # 若抱錯
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa5 in position 1273: invalid start byte
    # 刪除該資料夾的內容 %USERPROFILE%\AppData\Local\torch_extensions\torch_extensions\Cache
    ```
4. 測試
   1. 資料集打包
        ```ps1
        # python dataset_tool.py --source={原始圖片目錄} --dest={./datasets/your_data.zip}
        python dataset_tool.py --source=D:\reserch\preImage\black_core --dest=D:\reserch\black_core_dataset.zip --resolution=256x256
        ```
   2. 訓練
        > 產出模型pki檔案
        ```ps1
        # python train.py --outdir=./training-runs --cfg=stylegan3-t --data=./datasets/your_data --gpus=1 --batch=8 --fp16=True --gamma=8 --mirror=1

        # vram不足
        python train.py --outdir=D:\reserch\outtest --cfg=stylegan3-t --data=D:\reserch\black_core_dataset.zip --gpus=1 --batch=32 --batch-gpu=16 --gamma=10 --snap=10
        ```
   3. 產圖
        ```ps1
        python gen_images.py --outdir=out --trunc=1 --seeds=2 --network=https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-afhqv2-512x512.pkl
        ```

# conda操作
```ps1
# 查詢conda下有多少個虛擬環境
conda env list

# 啟用虛擬環境
conda activate {ENVIRONMENT}    # stylegan3,base

# 停用虛擬環境
conda deactivate

# 刪除虛擬環境
conda remove --name {ENVIRONMENT} --all
```