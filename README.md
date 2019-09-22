# PAAS
Passwd as a Service is a minimal HTTP web service that exposes the user and group information on a UNIX-like system.


## Installation
Update and or upgrade packages
```bash
apt-get update && apt-get upgrade
```

Use the package manager pip for installation of required packages. Run at PAAS/ directory. Passwd as a Service supports both python2 and python3
```bash
pip install -r requirements.txt
export PATH=$PATH:~/.local/bin/
```
### Running web service
```bash
$cd passwd_as_a_service/
$gunicorn -w 4 --threads 12 -b 0.0.0.0:5000 app:app
```
Webserver is now up and running.
```bash
Example:
http://localhost:5000/users
Response:
[
  {
    "comment": "root", 
    "gid": "0", 
    "home": "/root", 
    "name": "root", 
    "shell": "/bin/bash\n", 
    "uid": "0"
  }, 
  {
    "comment": "daemon", 
    "gid": "1", 
    "home": "/usr/sbin", 
    "name": "daemon", 
    "shell": "/usr/sbin/nologin\n", 
    "uid": "1"
  }
]
```

## Installation for Docker
Download and install 
[docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) for Linux Ubuntu systems

### Once docker is installed
```bash
bash build_and_run_docker.sh
```
The run_me.sh file will build and run the docker container. To verify the container is up and running use. This will show which containers are currently running. 
```bash
sudo docker ps -a
```
Open browser.
```bash
Example:
http://localhost:5000/users
Response:
An array of users on /etc/passwd
[
  {
    "comment": "root", 
    "gid": "0", 
    "home": "/root", 
    "name": "root", 
    "shell": "/bin/bash\n", 
    "uid": "0"
  }, 
  {
    "comment": "daemon", 
    "gid": "1", 
    "home": "/usr/sbin", 
    "name": "daemon", 
    "shell": "/usr/sbin/nologin\n", 
    "uid": "1"
  }
]
```

## Testing
Testing can be run from PAAS/ directory
```bash
python -m unittest discover -v
```

## Project Sturcture
```
+-- PAAS
| +-- Dockerfile
| +-- passwd_as_a_service
    | +-- src
        | +-- app.py
        | +-- cloud_service.py
        | +-- __init__.py
    | +-- test
        | +-- __init__.py
        | +-- test_cloud_service.py 
| +-- build_and_run_docker.sh
| +-- README.md
| +-- requirements.txt 
```
Project Sturcture
