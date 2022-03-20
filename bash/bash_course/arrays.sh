#!/usr/bin/env bash

# arrays: ( data data data data ) no commas, spaces only
numbers=(1 2 3 4 5 6)

# @ all elements
echo ${numbers[@]}
echo ${numbers[1]}
echo ${numbers[@]:1:3}
echo

# append arrays to another array.
numbers+=(a)

echo ${numbers[@]}

unset numbers[3]

echo ${numbers[@]}

# ! shows list indices of array elements. unset removes index.
echo ${!numbers[@]}

numbers[0]=1

echo ${numbers[@]}

for (( i = 0; i < 10; i++ )); do
    echo $i
done

echo

for i in "${numbers[@]}"; do
    echo $i
done
