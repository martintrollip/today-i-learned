- Date : 2020-05-11
- Tags : #Docker

## Basics

The basic Docker commands are

- build image `docker build --rm -t httpd-conf-project .`
- run `docker run -p 80:80 -p 443:443 httpd-conf-project` or
- run with virtual directory mounted `docker run -v /usr/local/applications/app/local-docs/:/usr/local/applications/app/webdoc/ -d -p 80:80 -p 443:443 httpd-conf-project`
- get list of all running docker instances `docker ps`, this shows the instance *NAME*
- stop a docker instance `docker stop {NAME}` or `docker kill {NAME}` (forced)
- executing an interactive command against a running docker instance `docker exec -i -t {NAME} /bin/bash`


[Docker run reference](docs.docker.com/engine/reference/run/)
