#!/bin/bash
# this is a comment

age=29

#if [ "$age" -gt 18 -a "$age" -lt 30 ]
#if [[ "$age" -gt 18 && "$age" -lt 30 ]]
if [ "$age" -gt 18 ] && [ "$age" -lt 30 ]
then
  echo "age: $age is valid  "
  else
  echo "age: $age in NOT valid"
fi

#if [ "$age" -gt 18 -o "$age" -lt 30 ]
#if [[ "$age" -gt 18 || "$age" -lt 30 ]]
if [ "$age" -gt 18 ] || [ "$age" -lt 30 ]
then
  echo "age: $age is valid  "
  else
  echo "age: $age in NOT valid"
fi

