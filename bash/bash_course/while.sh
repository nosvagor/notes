#!/usr/bin/env bash

# ┬ ┬┬ ┬┬┬  ┌─┐
# │││├─┤││  ├┤
# └┴┘┴ ┴┴┴─┘└─┘

# read -p "Enter number: " num
while [[ $num -gt 10 ]]; do
    echo $num
    num=$(( $num - 1 ))
done

# ┌─┐┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐
# │ ┬├┤  │ │ │├─┘ │ └─┐
# └─┘└─┘ ┴ └─┘┴   ┴ └─┘

while getopts "f:c:" opt; do
    case "$opt" in
        c )
            result=$(echo "scale=2; ($OPTARG * (9 / 5)) + 32" | bc)
            ;;
        f )
            result=$(echo "scale=2; ($OPTARG - 32) * (5 / 9)" | bc)
            ;;
        \? )
            echo "Invalid option"
            ;;

    esac
done

echo $result

while read line; do
    echo "$line"
done < <(ls $HOME)
