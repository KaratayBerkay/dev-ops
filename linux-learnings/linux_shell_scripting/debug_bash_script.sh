#!/bin/bash
# bash -x run command
set -x  # Run debug normally

echo "pid is $$"  # PID of script is printed

set +x  # Run debug mode

while (( COUNT < 10 )); do
  sleep 10
  (( COUNT++ ))
  echo $COUNT
done
