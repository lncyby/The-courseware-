#!/bin/bash

a=1
b=0
while ((a<=10))
do
    let "b += a"
    let "a++"
done
echo "1+2+3+...+10=$b"

