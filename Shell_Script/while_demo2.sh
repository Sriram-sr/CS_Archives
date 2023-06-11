#!/bin/zsh

num=5

while (($num>=1))
do
    echo $num
    num=$(($num-1))
done    

echo ""
echo ""

num=25

while (($num > 0))
do
	echo $num
	num=$(($num-5))
done
