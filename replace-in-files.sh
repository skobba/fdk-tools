#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo Illegal number of parameters
    echo Usage: replace-in-files.sh path filtype searchtext replacetext
    exit 0
fi

# echo path: $1
# echo filtype: $2
# echo searchtext: $2
# echo replacetext: $3


find $1 -name "*.scss" -type f -exec sed -i '' "s/$3/$4/g" {} +

