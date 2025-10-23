# uv筆記

## 安裝
* macOS/Liunx 
    ```ps1
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
* Windows 

    ```ps1
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

## 使用
### uv指令
```ps1
# 建立專案並指定python版本
uv init

# 建置venv環境並指定python版本
uv venv --python 3.13

# # 環境內安裝pip套件
# uv add requests

# 環境內安裝requirements.txt中的pip套件
uv add -r requirements.txt

# 在隔離環境中執行腳本
uv run main.py
```
### 進出環境及操作
> 其實能透過`uv指令`直接運行，但起
```
# 啟動虛擬環境
.venv\Scripts\activate

# 啟動專案
python main.py

# 處理完畢後停用
deactivate
```