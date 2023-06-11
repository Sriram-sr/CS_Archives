#!/bin/zsh

list=(2 6 7 8 4 1)

for ((i=0;i<${#list[@]};i++))
do	
    echo $list[$i]
done


for j in $list
do
    echo $list[$j]
done    

