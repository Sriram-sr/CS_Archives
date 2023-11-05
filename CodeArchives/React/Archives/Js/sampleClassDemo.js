// class Sample{
//     constructor(name, age, place){

//     }
// }
"usestrict"


let objectMap = {
    name: 'Sriram',
    age: 23,
    display : function(){
        return `${this.name} is ${this.age} years old`;
    }
}

const thisVerify = () => {
    console.log(this);
}

thisVerify();