#!/bin/bash

path=~/github_brreg/concept-catalogue-gui/src
replace_list=./fdk-rename-list.txt
file_type="*.scss"

IFS=$'\n'       # make newlines the only separator
set -f          # disable globbing
for i in $(cat < "$replace_list"); do

    IFS=' ' read -ra VALUES <<< "$i"    #Convert string to array
    #echo Old: ${VALUES[0]} - New: ${VALUES[1]}

    ./replace-in-files.sh $path $file_type ${VALUES[0]} ${VALUES[1]}
done
