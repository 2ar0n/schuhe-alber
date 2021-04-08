#!/bin/sh

if [[ $(command -v podman) ]]; then
    COMMAND="sudo podman"
elif [[ $(command -v docker) ]]; then
    COMMAND="docker"
fi

$COMMAND run -it -v "$PWD":/tmp/site/build localhost/tailwindcss npx tailwind build build/tailwind.css -c build/tailwind.config.js -o build/styles.css
