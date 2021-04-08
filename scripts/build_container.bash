#!/bin/sh

if [[ $(command -v podman) ]]; then
    COMMAND="sudo podman"
elif [[ $(command -v docker) ]]; then
    COMMAND="docker"
fi

$COMMAND build . -t tailwindcss
