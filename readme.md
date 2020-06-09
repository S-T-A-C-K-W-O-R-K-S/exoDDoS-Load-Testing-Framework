### exoDDoS
Enterprise-Grade Python Load/Performance Testing Framework

***

### Quick Start

1. navigate to the exoDDoS directory, if not already in that context
2. install the exoDDoS requirements by executing:
    - `python -m pip install -r requirements.txt` on Windows
    - `pip install -r requirements.txt` on UNIX-based systems
3. execute `locust --config exoddos.conf` to launch the framework

***

### Run Via Docker

> One-Time Commands

1. `docker build -t exoddos:1.1.1 .`
2. `docker run -it --name exoddos -p 5557:5557 -p 8089:8089 exoddos:1.1.1`

> Reuse exoDDoS Container

3. `docker start -ai exoddos`
4. `docker stop exoddos`

> Run As Debug User

It is possible to run exoDDoS from a Docker container as a single ephemeral user, for debugging purposes, which overrides the built-in credentials file. To do so, append the `-e debug-user="USERNAME"` and `-e debug-pass="PASSWORD"` flags while executing the run command for the Docker container.

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

*Updating the requirements as per the steps above will convert the requirements file to UCS-2 LE BOM (UNICODE) format so make sure to convert it back to UTF-8 without BOM (ASCII) format, otherwise some GIT clients will see it as a binary file rather than a text file and won't be able to properly resolve the deltas. Alternatively, update the requirements by executing `python -m pip freeze | Out-File -Encoding ASCII requirements.txt` on Windows or `pip freeze | Out-File -Encoding ASCII requirements.txt` on UNIX-based systems.*

> Prune Docker Images

To start fresh in Docker, execute `docker system prune` and then type `y` when prompted to. Make sure to read carefully what images you are pruning, as this will delete all Docker images currently present on the system.

> Accessing The WEB UI

By default, the WEB UI runs on `http://:8089` which makes `http://localhost:8089` available even when running exoDDoS from within a Docker container. Setting the `--web-host` config flag for the framework to a custom IP address may require additional Docker image configuration in order to be able to access the WEB UI for an instance of exoDDoS running inside a Docker container.
