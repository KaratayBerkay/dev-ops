#!/bin/bash
#  kill -l will list terminate commands
trap "echo Exit command Wıth SIGINT interrupt is detected" SIGINT  # CTRL + C
trap "echo Exit command Wıth SIGKILL terminate is detected" SIGKILL  # CTRL + Z
# SIGKILL && SIGSTOP

echo "pid is $$"  # PID of script is printed
while (( COUNT < 10 )); do
  sleep 10
  (( COUNT++ ))
  echo $COUNT
done

# man 7 signal
# trap any command signal command with
echo "Hello World"
exit 0
