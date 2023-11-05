let text = "";

function foreach(value, index, array){
    console.log(index);
    text += value+"<br>"
    document.getElementById('numbers').innerHTML = text;
}

function mapEachValues(value, index, array){
    return value*3;
}

function filtervalues(value, index, array){
    return value > 10;
}

function reduceFun(total, value, index, array){
    console.log(total);
    return total+=value;
}

function everyTrueCheck(value, index, array){
    return value > 18;
}

function someCheck(value, index, array){
    return value > 10;
}


