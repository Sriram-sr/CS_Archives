#!/bin/zsh

num=10

while [ $num -ge 1 ]
do
    if [ $num -eq 5 ]
    then 
        num=`expr $num - 1`
        continue
    fi
    echo $num
    num=`expr $num - 1`
done    
