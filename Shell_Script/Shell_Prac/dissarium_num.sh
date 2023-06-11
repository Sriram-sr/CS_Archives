#!/bin/zsh

num=(1 7 5)
square=1
result=0

for i in $num
do
    mul=$(($i**$square))	 
    result=$(($result+$mul))
    square=$(($square+1))
done    


#echo "The result is $result"

if [ $result -eq $num ]
then
    echo "It's a dissarium number"
else
    echo "It's not a dissarium number"
fi    
