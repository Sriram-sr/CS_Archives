#!/bin/zsh

for i in {1..5}
do
	for j in {1..$i}
	do
	     printf "#"
	done
	echo ""

done

for k in {5..1}
do
	for l in {1..$k}
	do
		printf "#"
	done
	echo ""
done
