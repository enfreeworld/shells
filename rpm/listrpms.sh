#!/bin/sh
find . -iname "*.rpm" | sed -e "s/x86_64.rpm//;s/noarch.rpm//" | sed -e "s/\([0-9]\).[a-zA-Z.0-9]*$/\1/" | sed -e "s#^./##"
