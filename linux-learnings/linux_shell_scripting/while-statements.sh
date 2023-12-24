#!/bin/bash
# this is a comment

#gnome-terminal

n=1
until [ $n -gt 7 ]; do
    echo "$n"
    #n=$(( n+1 ))
    sleep 0.3
    (( ++n ))
done

#while read p
#do
#  echo $p
#done < while-statements.sh
