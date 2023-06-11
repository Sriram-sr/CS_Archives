#!/bin/zsh

num=1

while [ $num -lt 10 ]
do
    echo $num
    if [ $num -eq 5 ]
    then
        break
    else
        num=`expr $num + 1`	    
    fi
done    
