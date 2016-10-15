#! /bin/bash

j=0

for ((i=0;i<11;i++))
do
    
    let "ret = i ** 2"
    let "j = j + ret"

done

echo "$j"





