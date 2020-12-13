#!/bin/bash

# Note that this script uses GNU-style sed. On Mac OS, you are required to first
#    brew install gnu-sed
#
# and then change your PATH to
#    PATH="/usr/local/opt/gnu-sed/libexec/gnubin:$PATH"
cat ../data/train_pos.txt ../data/train_neg.txt | sed "s/ /\n/g" | grep -v "^\s*$" | sort | uniq -c > ../data/vocab/vocab.txt
