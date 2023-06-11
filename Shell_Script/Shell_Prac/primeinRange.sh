#!/bin/zsh

primeArray=()

for i in {2..50}
do
	for j in {2..$i}
	do
		if (($i % $j==0))
		then
			break
		fi
	done
	echo $i
done
