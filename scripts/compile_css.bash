#!/bin/sh

if [[ $(command -v podman) ]]; then
    COMMAND="sudo podman"
elif [[ $(command -v docker) ]]; then
    COMMAND="docker"
fi

$COMMAND run -it -v "$PWD":/tmp/site localhost/tailwindcss npx tailwindcss-cli@latest build -o styles.css
