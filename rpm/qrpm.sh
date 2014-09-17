#!/bin/bash
for i in $@
do
    rpm -qi $i 1>/dev/null 2>&1 2>&1 && echo $i
done
