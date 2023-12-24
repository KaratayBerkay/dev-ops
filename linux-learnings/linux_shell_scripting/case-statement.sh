#!/bin/bash
# this is a comment

# First attribute given in command line
vehicle=$1

case $vehicle in
  "car" )
    echo "Rent of $vehicle is 100 points";;
  "van" )
    echo "Rent of $vehicle is 100 points";;
  * )
    echo "None found"
esac

echo -c "Enter some character : \c"
read value

case $value in
  [a-z] )
    echo "Rent of $vehicle [A-Z]";;
  [A-Z] )
    echo "Rent of $vehicle [a-z]";;
  [0-9] )
    echo "Rent of $vehicle [0-9]";;
  ? )
    echo "Rent of $vehicle with a special character "
  * )
    echo "None found"
esac
#case expression in
#  pattern1
#    statements ;;
#  pattern2
#    statements ;;
#  ...
#esac


