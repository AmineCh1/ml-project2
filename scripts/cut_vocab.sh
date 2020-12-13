#!/bin/bash

# Note that this script uses GNU-style sed. On Mac OS, you are required to first
#    brew install gnu-sed
#
# and then change your PATH to
#    PATH="/usr/local/opt/gnu-sed/libexec/gnubin:$PATH"
cat ../data/vocab/vocab.txt | sed "s/^\s\+//g" | sort -rn | grep -v "^[1234]\s" | cut -d' ' -f2 > ../data/vocab/vocab_cut.txt
