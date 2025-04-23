# 準備
* windows11
* git
* nvidia顯卡
* conda環境
  * anaconda/miniconda擇一
* 放github專案的資料夾
  * "$env:USERPROFILE\Documents\github.com"



# 建置
```ps1
# 建立放github專案的資料夾
New-Item "$env:USERPROFILE\Documents\github.com" -ItemType Directory -ea 0
cd "$env:USERPROFILE\Documents\github.com"

# 下載專案
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI

# 建立環境
conda create -n comfyui python=3.11
conda activate comfyui
pip install -r requirements.txt

# 安裝cuda版本的pytorch
conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.1 -c pytorch -c nvidia

# 啟動並listen
python main.py --listen 0.0.0.0
```



# 啟動SERVER
```ps1
# 啟用conda環境comfyui
conda activate comfyui

# 進入comfyui_home
cd "$env:USERPROFILE\Documents\github.com\ComfyUI"

# 啟動並listen any
python main.py --listen 0.0.0.0
```

# 模型下載
## civitai
> * 下載時帶入token
> * https://civitai.com/api/download/models/${modelId}?format=SafeTensor&size=full&allowNsfwContent=true&forceDownload=false&token=${token}

## huggingface
> * https://huggingface.co/${repo_id}/resolve/main/${filename}
