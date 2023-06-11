#!/bin/zsh

arg_func(){
	echo "Function name is the first argument which is $0"
	echo "First argument when calling function is $1"
	echo "Second argument when calling function is $2"
}

arg_func hello Shell 

echo "The return value of the function is $?"
