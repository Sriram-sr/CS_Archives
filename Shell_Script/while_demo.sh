#!/bin/zsh

var=10

while [ $var -gt 0 ]
do 
    echo $var
    var=`expr $var - 1`
done    

echo ""
echo ""

var=10

while (($var>0))
do
	echo $var
	var=$(($var-1))
done
