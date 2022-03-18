#!/usr/bin/env bash

# Author: cullyn
# Date Created: March, 17 2022
# Last Modified: March, 17 2022

# Description
# practice file for variables and parameter expansion.

# Usage
# vars.sh

# User defined variables: pref use lower case.
student="cullyn"

# Parameter: ${variable} -> pass variable by reference, and do other stuff (expansion).
# $variable -> used for simple variable reference.

echo "Hello ${student}"

# Shell variables: pref upper case; created by the shell, can be overwritten, but don't.
echo "Path: $PATH"
echo "User: $USER"
echo "Host: $HOSTNAME"
echo "HostType: $HOSTTYPE"
echo "prompt string 1: $PS1" # shell prompt

# Parameter expansion:
student="CuLlYN"

# case modification
echo "lowercase first: ${student,}"
echo "lowercase All: ${student,,}"
echo "uppercase first: ${USER^}"
echo "uppercase all: ${USER^^}"

# string len
echo "variable len #: ${#USER}"

# slicing
numbers=0123456789
echo ${numbers:0:5}
echo ${numbers:6}

# use space for negative offset
echo ${numbers: -3}
echo ${numbers: -3:2}
