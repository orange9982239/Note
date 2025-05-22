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
2. 用conda建置
   1. yolo-v8-cu118
    ```ps1
    # 建立python3.12環境，取名yolo-v8
    conda create -n yolo-v8-cu118 python=3.12 -y
    # 進入環境
    conda activate yolo-v8-cu118

    # 安裝ultralytics，他會安裝CPU版本的tourch
    pip install ultralytics

    # 測試(目前應該是CPU模式)
    yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"

    # 安裝cuda 11.8
    conda install nvidia/label/cuda-11.8.0::cuda-toolkit -y
    # cuda驗證
    nvidia-smi
    # nvcc驗證
    nvcc --version
    # conda安裝CUDA版本pytorch(https://pytorch.org/get-started/previous-versions/)
    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu118

    # 檢查關鍵套件版本
    python -c "import torch; print(f'PyTorch: {torch.__version__}')"
    python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
    python -c "import torch; print(f'CUDA device count: {torch.cuda.device_count()}')"
    python -c "import torch; print(f'CUDA device name: {torch.cuda.get_device_name(0)}')"

    # 測試(查看輸出是否由GPU進行)
    yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
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