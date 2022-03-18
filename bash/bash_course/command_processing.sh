#!/usr/bin/env bash

###############################################################################
# Author: cullyn
# Date Created: March, 18 2022
# Last Modified: March, 18 2022

# Description:
# scratch file for testing and learning concepts related to how bash processes
# commands, i.e., via:
# 1. Tokenization
# 2. Command Identification
# 3. Expansion
# 4. Quote Removal
# 5. Redirection

# Usage:
# command_processing.sh
###############################################################################

# ╔╦╗┌─┐┬┌─┌─┐┌┐┌┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
#  ║ │ │├┴┐├┤ ││││┌─┘├─┤ │ ││ ││││
#  ╩ └─┘┴ ┴└─┘┘└┘┴└─┘┴ ┴ ┴ ┴└─┘┘└┘

# Meta characters: | & ; () <> space, tab, newline
#   - Word: does not contain meta character.
#   - Token: contains a meta character.

# Combinations of these meta characters can be used to create control and
# redirection operators; they only matter if unquoted.

# ╦┌┬┐┌─┐┌┐┌┌┬┐┬┌─┐┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
# ║ ││├┤ │││ │ │├┤ ││  ├─┤ │ ││ ││││
# ╩─┴┘└─┘┘└┘ ┴ ┴└  ┴└─┘┴ ┴ ┴ ┴└─┘┘└┘

echo a b c echo 1 2 3
echo a b c; echo 1 2 3

# Simple command: list of words separated by newlines or other control
# operators.

# First word: interpreted as the command name, following words are arguments.

# Compound commands: give bash it's programming constructs.

# ╔═╗─┐ ┬┌─┐┌─┐┌┐┌┌─┐┬┌─┐┌┐┌
# ║╣ ┌┴┬┘├─┘├─┤│││└─┐││ ││││
# ╚═╝┴ └─┴  ┴ ┴┘└┘└─┘┴└─┘┘└┘

# 1. Brace expansion {list}, {start..stop..step}
# 2. Other expansions (left to right)

echo $USER has {1..3} apples and $(( 5 + 2 )) oranges

# 3. Word splitting: splitting of some unquoted words into separate words; is
# only performed on parameter expansions, command substitutions, and arithmetic
# expansions.

# Internal Field Separator (IFS) variable: default space, tab, and newline.

echo ${IFS@Q}
echo ${IFS}

numbers="1 2 3 4 5"
touch $numbers
ls
rm {1..5}

echo " "

numbers=1,2,3,4,5
touch $numbers
ls
rm $numbers

echo " "

IFS=","
echo ${IFS@Q}
touch $numbers
ls
rm {1..5}

# 4. Globbing

# Globbing: shortcut used to list files commands should operate on; only
# performed on words.

# Patterns are words that contain special pattern characters: * ? []
# Patterns are replaced with filenames that match the pattern.

# * -> matches anything (0 or more).
# ? -> matches any single character.
# [] -> matches [...] any characters inside the bracket (only 1, however); like
# regex, can be a range.

# ╔═╗ ┬ ┬┌─┐┌┬┐┌─┐  ╦═╗┌─┐┌┬┐┌─┐┬  ┬┌─┐┬
# ║═╬╗│ ││ │ │ ├┤   ╠╦╝├┤ ││││ │└┐┌┘├─┤│
# ╚═╝╚└─┘└─┘ ┴ └─┘  ╩╚═└─┘┴ ┴└─┘ └┘ ┴ ┴┴─┘

# Quote types: \ '' ""

# Quote removal removes all unquoted quote types that did not result due to
# shell expansion.

# ╦═╗┌─┐┌┬┐┬┬─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
# ╠╦╝├┤  │││├┬┘├┤ │   │ ││ ││││
# ╩╚═└─┘─┴┘┴┴└─└─┘└─┘ ┴ ┴└─┘┘└┘

# Redirection: determining where standard input[<], output[>], error[2>] are
# directed.

# &> -> standard output and error
# >> append rather truncate
