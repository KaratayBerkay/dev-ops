#!/bin/bash
# this is a comment

os=('ubuntu' 'windows' 'kali')

echo "${os[@]}"   # Print all elements
echo "${os[0]}"   # Print first element
echo "${!os[@]}"  # Print indexes of array
echo "${#os[@]}"  # Print length of array

# append
os[3]='mac'
echo "${os[@]}"
unset os[2]
echo "${os[@]}"

string=akjsdkljaskldj
echo "${string[@]}"
echo "${#string[@]}"