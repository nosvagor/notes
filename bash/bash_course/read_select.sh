#!/usr/bin/env bash

# ┬─┐┌─┐┌─┐┌┬┐
# ├┬┘├┤ ├─┤ ││
# ┴└─└─┘┴ ┴─┴┘

# $REPLY default variable for user input

# read -p  "Input your first name: " name
# read -s -p  "Input your age: " age
# read -t 5 -p  "Input your location: " town

# echo "My name is $name"
# echo "I am $age"
# echo "I am from ${town:-earth}"

# ┌─┐┌─┐┬  ┌─┐┌─┐┌┬┐
# └─┐├┤ │  ├┤ │   │
# └─┘└─┘┴─┘└─┘└─┘ ┴

PS3="What is the day of the week?: "

select day in mon tue wed thu fri sat sun; do
    echo "The day of the week is $day"
    break
done

