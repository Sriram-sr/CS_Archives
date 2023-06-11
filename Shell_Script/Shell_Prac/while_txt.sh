#!/bin/zsh

default="Hello"

while [ $default != "bye" ]
do
    read default
    #default=$string
    echo "You entered $default"
done    
