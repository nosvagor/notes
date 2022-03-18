#!/usr/bin/env bash

# Command substitution: $(command) -> execute command, then expand.
time=$(date +%H:%m)

echo "Hello $USER, the time right now is: $time"

# Arithmetic expansion: $((expression))

x=7
y=2

# Variables can exclude $ in asthmatic expansion.
# Note: only ints can be used.
echo $(( x + y ))
echo $(( x % y ))
echo $(( x / y ))

# bc command: handles floats via pipe echo pipe into bc
echo "scale=1; 5/2" | bc

# Tilde expansion: expands from home directory; useful for expanding from
# certain users, or working directories.
echo ~
echo ~root
echo ~notauser

# ~+ -> $PWD
# ~- -~> $OLDPWD
echo ~-
echo ~+

# Brace expansion: {} expands to string lists or range lists.

# string list: must have no spaces
echo {a,19,z,42,barry}
echo {jan,feb,mar,apr,may,jun}

# range list: auto expansion over same type.
echo {1..10}
echo {10..1}
echo {a..z}
# start..stop..step
echo {0..100..5}
