#!/bin/bash
# this is a comment

num1=20
num2=15
num3=20.553
num4=15.773

echo $num1 , $num2
echo add $( expr $num1 + $num2 )
echo sub $(( num1 - num2 ))
echo div $(( num1 / num2 ))
echo mul $(( num1 * num2 ))
echo rem $(( num1 % num2 ))

echo "scale=4;$num3*$num4" | bc
echo "scale=2;sqrt($num1)" | bc -l
echo "scale=2;3^3" | bc

