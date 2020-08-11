### exoDDoS CSDB
Enterprise-Grade Python Load/Performance Testing Framework

***

### Quick Start

01. remote onto the `10.93.39.222` jump host
02. navigate to `da.tadnet.eu` and log into Citrix
03. launch the `RDP Client for Dev Zones` Citrix app
04. remote onto the `ebowd81.ecbt1.tadnet.net` jump host
05. establish an SSH connection to `10.229.16.225`, as per the following examples
    - `ssh xa_tabakov@csdxd02.ecbt1.tadnet.net`
    - `ssh xa_tanasev@csdxd02.ecbt1.tadnet.net`
06. log into the `finworksdev` Docker registry
07. pull the latest exoDDoS CSDB image
    - `docker pull finworksdev/exoddos-csdb:latest`
08. run a singleton exoDDoS CSDB container
    - `docker run -it --name exoddos -p 5557:5557 -p 8089:8089 finworksdev/exoddos-csdb`
09. in a browser, navigate to the Web UI running at `10.229.16.225:8089`
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
    - `docker pull finworksdev/exoddos-csdb:latest`
03. run a singleton exoDDoS CSDB container
    - `docker run -it --name exoddos -p 5557:5557 -p 8089:8089 finworksdev/exoddos-csdb`
04. in a browser, navigate to the Web UI running at `10.229.16.225:8089`
05. from the Web UI, set the runtime parameters and launch the framework
