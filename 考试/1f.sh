#!/bin/bash
b=0
for ((a=1;a<=10;a++))

do
    let "b=b += a"
done

echo "1+2+3+...+10=$b"

