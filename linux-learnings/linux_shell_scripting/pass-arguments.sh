#!/bin/bash
# this is a comment

echo " > name of sh $0 | passed argument = 1. $1 2. $2  3. $3"

args=("$@")

echo " > passed argument = 1. ${args[0]} 2. ${args[1]}  3. ${args[2]}"
echo "number of arg passed $#"
