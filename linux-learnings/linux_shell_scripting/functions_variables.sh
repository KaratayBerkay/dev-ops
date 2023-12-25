#!/bin/bash
# this is a comment

#function foo() {
#    echo "foo function +"
#}
#
#foo_other() {
#    local variable=$1
#    echo "$variable + $2 function +"
#}
#
#foo_other other next

is_file_exits() {
  local file="$1"
  [[ -f "$file" ]] && return 0 || return 1
}

if ( is_file_exits "$1" )
then
  echo "File is found"
else
  echo "File is NOT found"
fi
