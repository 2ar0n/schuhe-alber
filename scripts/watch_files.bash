#!/bin/bash

files=(base.html de.yaml it.yaml en.yaml)
len=${#files[@]}

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

while true; do
    hashes=()
    for (( n=0; n<len; n++ )); do
        hash=$(md5sum ${files[$n]})
        hash=($hash)
        hashes=(${hashes[@]} "$hash")
    done
    sleep 1
    for (( n=0; n<len; n++ )); do
        hash=$(md5sum ${files[$n]})
        hash=($hash)
        if [ "$hash" != "${hashes[$n]}" ]; then
            source "$DIR/compile_css.bash"
            python "$DIR/generate_pages.py"
        fi
    done
done
