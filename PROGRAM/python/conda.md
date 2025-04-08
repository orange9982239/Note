# conda

## miniconda
### 1. 安裝
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
## 可以使用conda指令
conda
## 可以進入conda預設的base環境
conda activate base
```

### 2. 操作
#### 2.1 conda操作
```ps1
# 列出conda下的全部虛擬環境
conda env list

# 進入虛擬環境(啟用)
conda activate {ENVIRONMENT}    # base,stylegan3

# 退出虛擬環境(停用)
conda deactivate

# 察看虛擬環境下的包
conda list -n {ENVIRONMENT}
```

#### 2.2 conda環境調整
```ps1
# 建立虛擬環境
conda create -n {ENVIRONMENT} python={PYTHON_VERSION} {PACKAGE_NAME}={PACKAGE_VERSION}
## 建立虛擬環境並安裝套件
## conda create -n test_env_310 python=3.10
## 建立虛擬環境並安裝套件
## conda create -n test_env_310_numpy python=3.10 numpy=1.23.5


# 刪除虛擬環境
conda remove --name {ENVIRONMENT} --all
```

#### 2.3 environment.yml
##### 範例
> 以下是一個簡單的 environment.yml 範例：
> - `name`: 環境名稱為 "myenv"
> - `channels`: 指定套件來源，優先使用 conda-forge，其次是 defaults
> - `dependencies`: 列出需要的套件
>   - 可以指定確切版本 (numpy=1.23.5)
>   - 可以指定最低版本 (pandas>=1.5.0)
>   - 可以不指定版本 (matplotlib)
>   - 可以通過 pip 安裝額外的套件
```yaml
name: myenv
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy=1.23.5
  - pandas>=1.5.0
  - matplotlib
  - pip
  - pip:
    - requests>=2.28.0
```
##### 建置環境
```ps1
# cd 到有environment.yml的資料夾
# 根據environment.yml建置conda環境
conda env create -f environment.yml

# 編輯完yml檔案後更新環境
conda env update --name {ENVIRONMENT} --file environment.yml --prune
```

