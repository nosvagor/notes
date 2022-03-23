#!/usr/bin/env bash

returning_strings () {
    echo "Hello, ${1} how are you doing today?"
}

check_factor () {
    base=$1
    factor=$2

    if [[ $(($base % $factor)) -eq 0 ]]; then
        echo true
    else
        echo false
    fi

    # or using Ternary
    (( base % factor )) && echo "false" || echo "true"
}

move () {
    echo $(( $position + 2 * $roll ))
}

count_to_twenty () {
    count=0

    while [[ $count -lt 21 ]]; do
        echo "Count: $count"
        (( count++ ))
    done
}

century_from_year () {
    year=$1

    # century=$(( year / 100 ))
    # (( year % 100 )) && echo $century || echo $(( century + 1 ))

    # better
    echo "$(( (year +99 ) / 100))"
}
