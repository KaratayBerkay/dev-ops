#!/bin/bash
# this is a comment

var=30

readonly var

var=50

hello() {
  echo "Hello World"
}

readonly -f hello

readonly  # print all readonly variables
