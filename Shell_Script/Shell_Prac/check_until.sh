#!/bin/zsh

num=10

until [ $num -le 0 ]
do
	echo "$num"
	num=$(($num-1))
done


