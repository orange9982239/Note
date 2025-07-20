#!/bin/sh

# 使用 curl 檢查本地 API Server 的 /healthz 端點
# 127.0.0.1:6443 是本地 API Server 的監聽地址
# --cacert, --cert, --key 是為了能通過 TLS 驗證，請根據您的實際路徑修改
# 如果您的 API Server 允許匿名訪問 /healthz，可以簡化 curl 命令

# 簡單的 TCP 檢查方式 (如果 API Server 無需 TLS 驗證或允許匿名)
# curl -k https://127.0.0.1:6443/healthz &> /dev/null
# if [ $? -eq 0 ]; then

# 更可靠的檢查方式：使用 netstat 檢查 6443 port 是否在監聽
if netstat -lntp | grep -q 6443; then
    exit 0 # 端口存在，返回成功
else
    exit 1 # 端口不存在，返回失敗
fi