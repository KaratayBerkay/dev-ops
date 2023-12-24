#!/bin/bash
# this is a comment

echo -e "Enter the name of file : \c"
read file_name

# A file exits or not
if [ -e $file_name ]
then
  echo "$file_name is found"
else
  echo "$file_name is not found"
fi

# Is it a file or not
if [ -f $file_name ]
then
  echo "$file_name is found"
else
  echo "$file_name is not found"
fi

# Check Directory
if [ -f $file_name ]
then
  echo "$file_name is found"
else
  echo "$file_name is not found"
fi
