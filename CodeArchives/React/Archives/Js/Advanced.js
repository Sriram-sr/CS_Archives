const mapList = new Map([
    ['BMW', 600000],
    ['Audi', 6001122],
    ['Rolls Royse', 1600000],    
])

mapList.forEach(function(value){
    console.log(value)
})

let num = String(12);
console.log(num, typeof num);

let str = '445';
let int_converted = parseInt(str);
console.log( int_converted, typeof int_converted );

console.log(Number("3.14"));
console.log(Number(Math.PI));
console.log(Number(""));
console.log(Number("fishe"));

let obj = {
    var1: 'string',
    var2: [1,2,3],
    var3: function(){
        console.log(this);
    }
};

console.log(obj.var3());