#!/bin/bash

SOURCE="/dfs01/data_source"                         # 來源(/結尾)
TARGET="/data_target"                               # 儲存目標
SSHSERVER="{account}@{ip}"                          # 遠端SERVER
SSHPORT="22"                                        # 遠端SERVER PORT
SYNCDAYS="5"                                        # 同步天數

rsync \
    -ahrv \
    --progress \
    --partial-dir=.rsync-partial \
    --files-from=<(find $SOURCE -mtime -$SYNCDAYS -type f -exec realpath --relative-to $SOURCE {} \;) \
    -e "ssh -p $SSHPORT -o ConnectTimeout=60 -ServerAliveInterval=60 -ServerAliveCountMax=2" \
    $SOURCE \
    "${SSHSERVER}:${TARGET}"