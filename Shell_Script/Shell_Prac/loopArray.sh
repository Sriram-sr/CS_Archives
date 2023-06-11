#!/bin/zsh

# values added
array=( "This" "is" "Dynamic" 2 3 "Array")

for char in ${array[*]}
do
    echo $char
done

#2nd method

for (( i=0; i<${#array[@]}; i++))
do
    #echo $array[i]
    echo ${array[$i]} #another meth
done    
