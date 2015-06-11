# Docker Link Helper [![Build Status](https://travis-ci.org/tback/docker-link-helper.svg?branch=master)](https://travis-ci.org/tback/docker-link-helper)

## Usage
Install via Dockerfile
```
RUN apt-get -y install python-setuptools 
RUN easy_install docker-link-helper
```

Run from entrypoint
```
# terminate entrypoint on error 
set -e

docker-link-helper --link alink --link anotherlink /some/file /some/other/file
```

This will search `/some/file` and `/some/other/file` for names of environment variables in chevrons (<>) and replace
them with their values. `<MYSQL_ENV_MYSQL_DATABASE>` is replaced by the value of the environment variable 
`$MYSQL_ENV_MYSQL_DATABASE`.
