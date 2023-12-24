#!/bin/bash
# this is a comment

for (( i=1; i<=10; i++ ))
do
  if [ $i -gt 7 -o $i -eq 3 ]
  then
    continue
  elif [ $i -eq 5 ]; then
      break
  else
    echo "$i"
  fi
done
