#!/bin/bash
# this is a comment

for var in 1 2
do
  echo $var
done

echo "Other for loop"

for var in {4..5}
do
  echo $var
done

echo "Other loop increment by 3"

for var in {2..5..3}
do
  echo $var
done

echo ${BASH_VERSION}
for (( i=0; i<5; i++ ))
do
  echo $i
done

for command in ls pwd date
do
  echo "--------------------$command--------------------"
  $command
  echo "--------------------$command--------------------"
done

