### exoDDoS CSDB
Enterprise-Grade Python Load/Performance Testing Framework

***

### Quick Start

01. remote onto the `x.x.x.x` jump host
02. navigate to `x.x.x` and log into Citrix
03. launch the `redacted` Citrix app
04. remote onto the `x.x.x.x` jump host
05. establish an SSH connection to `x.x.x.x`, as per the following examples
    - `ssh redacted@x.x.x.x`
    - `ssh redacted@x.x.x.x`
06. log into the `redacted` Docker registry
07. pull the latest exoDDoS CSDB image
    - `docker pull redacted:latest`
08. run a singleton exoDDoS CSDB container
    - `docker run -it --name exoddos -p 5557:5557 -p 8089:8089 redacted`
09. in a browser, navigate to the Web UI running at `x.x.x.x:8089`
10. from the Web UI, set the runtime parameters and launch the framework

### Subsequent Runs

01. start the exoDDoS CSDB container with an attached interactive terminal
    - `docker start -ai exoddos`
02. stop the running exoDDoS CSDB container
    - `docker stop exoddos`

### Subsequent Runs Following An Image Update

01. delete all local Docker data
    - `docker system prune --all --volumes`
02. pull the latest exoDDoS CSDB image
    - `docker pull redacted:latest`
03. run a singleton exoDDoS CSDB container
    - `docker run -it --name exoddos -p 5557:5557 -p 8089:8089 redacted`
04. in a browser, navigate to the Web UI running at `x.x.x.x:8089`
05. from the Web UI, set the runtime parameters and launch the framework
