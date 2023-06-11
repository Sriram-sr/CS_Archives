#!/bin/zsh

myfunc(){
	ping -c 1 $1 > /dev/null
	if [ $? -eq 0 ]
        then
            echo "$1 can be reached"
	    continue
	fi
	echo "$1 cannot be reached"
}


for i in 192.168.0.{110..120}
do 
    myfunc $i
done    


      	    
