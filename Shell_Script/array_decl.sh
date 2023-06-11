#!/bin/zsh

array=( 2 3 4 "Word" "l" "Letter")

echo $array[0]

echo ${array[@]}

echo ${array:2:8}  # it won't through index out of range error

echo ${array:1:3}

for [ i in array ]{
	echo $i
}

