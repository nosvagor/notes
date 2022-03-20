#!/usr/bin/env bash

# ┬  ┬┌─┐┌┬┐
# │  │└─┐ │
# ┴─┘┴└─┘ ┴

# list: one of more commands on a given line.
# & -> send to background.
# && -> run sequentially if prev is successful. (and)
# || -> runs if first one failed. (or)
# ; -> run in order they are given, same as new line.
# A && B || C -> A ? true (B) : false (C)

# ┌┬┐┌─┐┌─┐┌┬┐
#  │ ├┤ └─┐ │
#  ┴ └─┘└─┘ ┴

# [ test command ]: true = 0, false = 1 (swapped from other languages)
# [ must be a space ]
# -gt -lt -geq -leq -neq -eq -> INT test operators

[[ 2 -eq 2 ]] ; echo "true $?"
[[ 2 -eq 1 ]] ; echo "false $?"

# = != ... -> string test operators
# -z -> checks for length of zero
# -n -> checks if length is not zero

[[ -z $empty ]] ; echo "true $?"
[[ -n $empty ]] ; echo "false $?"

# -e -> check if file exists
# -f -> check if regular file exists
# -d -> check if directory exists
# -x -> check if script exists
# + lots of more.

[[ -e not_real.txt ]] ; echo "false $?"


# ┌─┐┌─┐┌┐┌┌┬┐┬┌┬┐┬┌─┐┌┐┌┌─┐┬
# │  │ ││││ │││ │ ││ ││││├─┤│
# └─┘└─┘┘└┘─┴┘┴ ┴ ┴└─┘┘└┘┴ ┴┴─┘

# if statements work by checking the exist status of a command (often a test command)

if [[ 2 -gt 1 ]]; then
    echo "if statement is true"
fi

if [[ 2 -eq 1 ]]; then
    echo "if statement is true"
elif [[ 1 -eq 1 ]]; then
    echo "second test passed"
else
    echo "this condition is false"
fi

# ┌─┐┌─┐┌─┐┌─┐
# │  ├─┤└─┐├┤
# └─┘┴ ┴└─┘└─┘

# replaces elifs if based on a single variable.

read -p "Please enter a number: " number
case "$number" in
    [0-9] )
        echo "number is between 0-9"
        ;;
    [0-9][0-9] )
        echo "number is double digit"
        ;;
    [0-9][0-9][0-9] )
        echo "number is 3 digit"
        ;;
    s)
        echo "not a int or greater than 3 digits"
esac
