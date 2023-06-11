#!/bin/zsh

add(){
	echo $1
	echo $2
	#result=`expr $1 + $2`
	#echo "Result is $result"
	result=$(($1+$2))
	echo "result is $result"
}	

echo "Enter first number"
read  num1
echo "Enter second number"

add $num1 $num2
