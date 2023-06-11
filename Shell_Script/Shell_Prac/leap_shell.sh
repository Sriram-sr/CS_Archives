#!/bin/zsh

echo "Enter a year"
read year

div4=`expr $year % 4`
div100=`expr $year % 100`
div400=`expr $year % 400`

if ([ $div4 -eq 0 ]) || ([ $div100 -ne 0] && [ $div400 -eq 0])
then
    echo "It's a leap year"
else 
    echo "It's a non leap year"
fi    
