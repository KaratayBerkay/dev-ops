#!/bin/bash
# this is a comment

echo "Enter name: "
read name
echo "Here is your name : $name"


echo "Enter name, age "
read name age
echo "Here is your name : $name, and here is your $age"

read -p "username : " username
read -sp "password : " password
echo "username : $username && $password"

# Extract variables like array
echo "Write 3 names to echo"
read -a names
echo "Names : ${names[0]}, ${names[1]}, ${names[2]}"

# Default collect variables on $REPLY
read
echo "Variable Input : $REPLY"

# Run script with . user_input.sh