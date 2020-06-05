### exoDDoS
Enterprise-Grade Python Load/Performance Testing Framework

***

### Quick Start

1. navigate to the exoDDoS directory, if not already in that context
2. install the exoDDoS requirements by executing...
    - `python -m pip install -r requirements.txt` on Windows
    - `pip install -r requirements.txt` on UNIX-based systems
3. execute `locust -f exoddos.py` to launch the framework

***

### Known Compatibility Table

| Locust Version | Python Version | Operating System |
|:--------------:|:--------------:|:----------------:|
| v1.0.3         | v3.8.3         | Windows 10       |
| v1.0.3         | v3.8.3         | Ubuntu 20        |
| v1.0.3         | v3.7.7         | CentOS 8         |

***

### Run Via Docker

> One-Time Commands

1. `docker build -t exoddos:1.0.3 .`
2. `docker run -it --name exoddos -p 5557:5557 -p 8089:8089 exoddos:1.0.3`

> Reuse exoDDoS Container

3. `docker start -ai exoddos`
4. `docker stop exoddos`

***

### Common [Command Line Options](https://docs.locust.io/en/stable/configuration.html#command-line-options)

| Option                  | Flag              | Example Command                              |
|:----------------------- |:----------------- |:-------------------------------------------- |
| Log File                | --logfile LOGFILE | `locust -f exoddos.py --logfile exoddos.log` |
| Distributed Mode Master | --master          | `locust -f exoddos.py --master`              |
| Distributed Mode Worker | --worker          | `locust -f exoddos.py --worker`              |

***

### Troubleshooting

> Clean Installation

1. upgrade PIP to the latest version by executing:
    - `python -m pip install --upgrade pip` on Windows
    - `pip install --upgrade pip` on UNIX-based systems
2. make a backup of the installed PIP packages by executing:
    - `python -m pip freeze > snapshot.txt` on Windows
    - `pip freeze > snapshot.txt` on UNIX-based systems
3. uninstall all PIP packages by executing:
    - `python -m pip uninstall -r snapshot.txt -y` on Windows
    - `pip uninstall -r snapshot.txt -y` on UNIX-based systems
4. navigate to the exoDDoS directory, if not already in that context
5. install the exoDDoS requirements by executing:
    - `python -m pip install -r requirements.txt` on Windows
    - `pip install -r requirements.txt` on UNIX-based systems

> Update Requirements

1. upgrade PIP to the latest version by executing:
    - `python -m pip install --upgrade pip` on Windows
    - `pip install --upgrade pip` on UNIX-based systems
2. make a backup of the installed PIP packages by executing:
    - `python -m pip freeze > snapshot.txt` on Windows
    - `pip freeze > snapshot.txt` on UNIX-based systems
3. uninstall all PIP packages by executing:
    - `python -m pip uninstall -r snapshot.txt -y` on Windows
    - `pip uninstall -r snapshot.txt -y` on UNIX-based systems
4. install the latest version of locust by executing:
    - `python -m pip install locust` on Windows
    - `pip install locust` on UNIX-based systems
5. navigate to the exoDDoS directory, if not already in that context
6. save all the freshly installed PIP packages as the new requirements by executing:
    - `python -m pip freeze > requirements.txt` on Windows
    - `pip freeze > requirements.txt` on UNIX-based systems
