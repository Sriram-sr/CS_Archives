num=5
res=1

while [ $num -gt 0 ]
do
    res=$(($num * $res))
    num=$(($num - 1))
done    

echo "The factorial of number is $res"
