function myfunc(){
    document.getElementById('check').innerHTML = 9+9;   
}

function alertIt(){
    // window.alert("This is an alert");
    alert("Alertsss");
}

function addName(){
    let fname, lname;
    fname = 'Sri';
    lname = 'ram';
    console.log(fname+' '+lname);
}

function addition(num1, num2){
    return num1+num2;
}

function subtraction(num1, num2){
    return num1-num2;
}

function multiplication(num1, num2){
    return num1*num2;
}
function division(num1, num2){
    return (num1/num2).toFixed(2);
}

let x = 2;
console.log(typeof x);
console.log(typeof division)