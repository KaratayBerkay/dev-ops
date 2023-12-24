#!/bin/bash
# Create a text.txt and append in it

# check read permission
if [ -r $file_name ]
then
    if [ -w $file_name ]
    then
      echo "$file_name is empty"
      cat >> $file_name
    fi
else
  echo "$file_name is NOT empty"
fi