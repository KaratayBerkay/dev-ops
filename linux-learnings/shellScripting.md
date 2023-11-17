Shell Scripting
===============

``` bash
xyz.sh
#! /bin/bash
# This is a comment
echo "Hello World"
cp $1 $2
grep $1 $2

read count
if [ $count -eq 100 ]
    then
    echo Success: $count
    else
    echo Failure: $count
fi

c=1
while [ $c -le 5 ]
do
    command1
    command2
done

for  i in 1 2 3 4 5
    do
    echo "Welcome $i times"
    done
```
give persmissions to .sh file : chmod a+x xyz.sh  # e.g -rwxr-xr-x
``` bash
./xyz.sh  # run shell
./xyz.sh arg1 arg2  # run shell with arguments
```

read - user input
``` bash
echo "Enter name"
read name
echo "Entered name is $name"
```

clear - clear screen
``` bash
echo "Enter name"
read name
clear
echo "Entered name is $name"
```

ping_s.sh
``` bash
#! /bin/bash
echo "Enter the IP address"
read ip
ping -c3 $ip > /dev/null  # so that output of ping is not displayed
if [ $? -eq 0 ]
    then
    echo "Server $ip is up"
    else
    echo "Server $ip is down"
fi
``` bash
