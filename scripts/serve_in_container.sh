#!/bin/sh

if [[ $(command -v podman) ]]; then
    COMMAND="sudo podman"
elif [[ $(command -v docker) ]]; then
    COMMAND="docker"
fi

$COMMAND run -dit --name apache-httpd -p 8080:80 -v "$PWD/_site":/usr/local/apache2/htdocs/ httpd:2.4