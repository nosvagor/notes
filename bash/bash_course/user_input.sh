#!/usr/bin/env bash

# ┌─┐┌─┐┌─┐┬┌┬┐┬┌─┐┌┐┌┌─┐┬    ┌─┐┌─┐┬─┐┌─┐┌┬┐┌─┐┌┬┐┌─┐┬─┐┌─┐
# ├─┘│ │└─┐│ │ ││ ││││├─┤│    ├─┘├─┤├┬┘├─┤│││├┤  │ ├┤ ├┬┘└─┐
# ┴  └─┘└─┘┴ ┴ ┴└─┘┘└┘┴ ┴┴─┘  ┴  ┴ ┴┴└─┴ ┴┴ ┴└─┘ ┴ └─┘┴└─└─┘

echo "Parameter $1"
echo "Parameter $2"
echo "Parameter ${3}"
echo "Parameter ${10:-none}"
echo "Parameter $11" # parameters over 9 need brace expansion. but like, do limit user position parameters.
echo " "

# ┌─┐┌─┐┌─┐┌─┐┬┌─┐┬    ┌─┐┌─┐┬─┐┌─┐┌┬┐┌─┐┌┬┐┌─┐┬─┐┌─┐
# └─┐├─┘├┤ │  │├─┤│    ├─┘├─┤├┬┘├─┤│││├┤  │ ├┤ ├┬┘└─┐
# └─┘┴  └─┘└─┘┴┴ ┴┴─┘  ┴  ┴ ┴┴└─┴ ┴┴ ┴└─┘ ┴ └─┘┴└─└─┘

# Special parameters: immutable parameters script based on current script.

# $# -> number of positional parameters.
# $0 -> current shell in terminal / name of script in script

echo "Total parameters given #: $#"
echo "Script name: $0"
echo " "

if [[ $# -ne 3 ]]; then
    echo "$(basename $0) requires 2 arguments"
    echo "Usage: $0 <file1> <file2> <file3>"
    exit 1
fi

# $@ -> $1 $2 $3 .. $N
# "$@" -> "$1" "$2" $"3" ... "$N"

echo "All parameters $@"

# $* -> $@

IFS=","
# "$*" -> inserts first IFS split char, instead of spaces like "$@"

echo "All parameters $*"

# ┬─┐┌─┐┌─┐┌┬┐
# ├┬┘├┤ ├─┤ ││
# ┴└─└─┘┴ ┴─┴┘


# ┌─┐┌─┐┬  ┌─┐┌─┐┌┬┐
# └─┐├┤ │  ├┤ │   │
# └─┘└─┘┴─┘└─┘└─┘ ┴
