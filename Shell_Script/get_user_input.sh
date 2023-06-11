#! /bin/bash  
#above line tells which intepreter has to exceute

echo "Enter any Name"
#sleep 1
read Name
echo "Hello $Name"
#sleep 2 
echo "Hello Shell"

unset Name  # this is used to delete a variable

echo "Now I'm printing $Name"

echo -n "Next line will be appended as n flag is used"

echo " appended"

# getting double input 

echo "Enter two space seperated numbers"
read start stop
sleep 1
echo "First number is $start"
echo "Second number is $stop"
