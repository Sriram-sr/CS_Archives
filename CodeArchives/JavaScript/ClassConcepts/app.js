class BaseClass{
    constructor(name, age, place){
        this.name = name;
        this.age = age;
        this.place = place;
    }

    displayProperties(){
        console.log(`The name of Person is ${this.name} age is ${this.age} and he\'s from ${this.place}`);
    }
}

let baseInstance = new BaseClass('Vijay', 23, 'Kallakurichi');
baseInstance.displayProperties();

