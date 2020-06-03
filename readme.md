## exoDDoS
Enterprise-Grade Python Load/Performance Testing Framework

***

### Known Compatibility Table

| Locust Version | Python Version | Operating System        | Install                                          |
|:--------------:|:--------------:|:-----------------------:|:------------------------------------------------:|
| v0.14.6        | v3.7.7 x64     | Windows 10 Professional | pip install 'locustio==0.14.6' --force-reinstall |
| v0.14.6        | v3.7.7 x64     | Ubuntu 20               | pip install 'locustio==0.14.6' --force-reinstall |
| v0.14.6        | v3.7.7 x64     | CentOS 8                | pip install 'locustio==0.14.6' --force-reinstall |

***

### Run Via Docker

> One-Time Commands

1. `docker build -t exoddos:0.14.6 .`
2. `docker run -it --name exoddos -p 5557:5557 -p 8089:8089 exoddos:0.14.6`

> Reuse exoDDoS Container

3. `docker start -ai exoddos`
4. `docker stop exoddos`

***

### Full List Of Commands For Satisfying Dependencies On CentOS 8.x Boot (Minimal Install)

```
sudo dnf update -y
sudo dnf install python3 python3-devel python3-setuptools python3-wheel -y
sudo dnf install gcc openssl-devel bzip2-devel libffi-devel -y
sudo dnf install make -y

cd /usr/src

sudo wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz
sudo tar xzf Python-3.7.7.tgz
sudo rm Python-3.7.7.tgz

cd Python-3.7.7

sudo ./configure --enable-optimizations
sudo make altinstall

sudo pip3 install 'locustio==0.14.6' --force-reinstall
```

***

### Command Line Options

| Run exoDDoS With... | Command                                         |
|:------------------- |:----------------------------------------------- |
| ...Log File         | `locust -f exoddos.py --logfile=exoddos.log`    |
| ...Console Logging  | `locust -f exoddos.py`                          |
