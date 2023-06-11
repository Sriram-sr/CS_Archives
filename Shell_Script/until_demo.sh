#!/bin/zsh

num=1

until [ ! $num -lt 10 ]
do
    echo $num
    num=`expr $num + 1`
done    
