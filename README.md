# Docker Link Helper [![Build Status](https://travis-ci.org/tback/docker-link-helper.svg?branch=master)](https://travis-ci.org/tback/docker-link-helper)

## Usage
Install via Dockerfile
```
apt-get -y install python-pip 
pip install docker-link-helper
```

Run from entrypoint
```
docker-link-helper --link alink --link anotherlink /some/file /some/other/file
```
