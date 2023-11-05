let number = 5;

function sumOfSeries(number){
    let sumOfValues = 0;
    while (number>0){
        sumOfValues+=number;
        number-=1;
    }
    
    return sumOfValues;
}

console.log(sumOfSeries(number));