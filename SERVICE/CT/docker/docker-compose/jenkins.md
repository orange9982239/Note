# jenkins

``` yaml
version: '3.8'
services:
  jenkins:
    container_name: jenkins
    image: jenkins/jenkins:lts
    privileged: true
    user: root
    ports:
      - 8080:8080
      - 50000:50000
    volumes:
      - /srv/jenkins:/var/jenkins_home
```

# 執行PYTHON SCRIPT
1. 登進container安裝python3及pip
2. 用heredoc，執行python script
```sh
python3 <<- PYTHON_SCRIPT
cars = ["Ford", "Volvo", "BMW"]
carsMapObj = map(
    lambda x: {
        "key1":x,
        "key2":f"{x}_001"
    }, 
    cars
)
print(list(carsMapObj)) 
PYTHON_SCRIPT

## output
# Started by user administrator
# Running as SYSTEM
# Building in workspace /var/jenkins_home/workspace/Python/test
# [test] $ /bin/sh -xe /tmp/jenkins2308651436959623755.sh
# + python3
# [{'key1': 'Ford', 'key2': 'Ford_001'}, {'key1': 'Volvo', 'key2': 'Volvo_001'}, {'key1': 'BMW', 'key2': 'BMW_001'}]
# Finished: SUCCESS
```
3. tip
  * 注意是python3，作業系統似乎內置了python2
  * 建議先寫好python
      * 若引用pip包，需要先進container安裝
      * 在container嘗試執行
      * 再丟進heredoc
* 參考
  https://zh.wikipedia.org/zh-tw/Here%E6%96%87%E6%A1%A3