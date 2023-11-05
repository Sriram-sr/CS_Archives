let dict_alike = {
    name: 'Sriram',
    age: 22
}

let copy_alike = {
    ...dict_alike,
    place: 'Cpt'
}

// console.log(copy_alike.place)

let array = [2,3,4,9,5,11];
let new_array = [];
let i;
for(i=0;i<array.length;i++){
    console.log(new_array);
    new_array.push(array[i]);
}

// console.log(new_array);

let bigger_array = new_array.filter( (number) => {
    return number>8;
});

console.log(bigger_array);
