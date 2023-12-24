#!/bin/bash
# this is a comment
count=10

if [ $count -eq 10 ]
then
  echo "Count is 10"
fi

if (( $count >= 10 ))
then
  echo "Count is 10"
fi

word=abc
if [[ $word == "abc" ]]
then
  echo "First Word is correct"
elif [[ $word == "abc1" ]]
then
  echo "Second  Word is b correct"
else
  echo "Else Word is NOT correct"
fi


#if [ condition ]
#then
#  statement
#fi

#-eq - is equal to -if [ "$a" -eq "$b" ]
#-ne - is not equal to -if [ "$a" -ne "$b" ]
#-gt - is not equal to -if [ "$a" -gt "$b" ]
#-ge - is not equal to -if [ "$a" -ge "$b" ]
#-lt - is not equal to -if [ "$a" -lt "$b" ]
#< - is not equal to -if [ "$a" -le "$b" ]
#<= - is not equal to -if [ "$a" -eq "$b" ]
#> - is not equal to -if [ "$a" -eq "$b" ]
#>= - is not equal to -if [ "$a" -eq "$b" ]

#string comparison
# =  - is equal to - if [ "$a" = "$b" ]
# == - is equal to - if [ "$a" == "$b" ]
# != - is not equal to - if [ "$a" != "$b" ]
# < - is less than, in ASCII alphabetical order - if [[ "$a" < "$b" ]]
# > - is less than, in ASCII alphabetical order - if [[ "$a" < "$b" ]]
# -z -string is null, that is, has zero length

