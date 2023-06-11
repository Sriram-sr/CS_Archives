#!/bin/zsh

#num=-12
echo "Enter any number"
read num

if [ $num -eq 0 ]
then
	echo "Number is Zero"
elif [ $num -gt 0 ] 
then 
	echo "Number is positive"
elif [ $num -lt 0 ]
then 
	echo "Number is negative"
fi
