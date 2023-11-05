class Player{
    constructor(name, age){
        console.log('player ', this);
        this.name = name;
        this.age = age;
    }

    introduce(){
        console.log(`Iam ${this.name} and my age is ${this.age}`);
    }
}

class Wizard extends Player{
    constructor(name, type){
        super(name, type);
        console.log('wizard ', this);
    }

    wiz_method(){
        console.log(`The parent properties gained are ${this.name} and ${this.age}`);
    }
}

let wiz1 = new Wizard('Sriram', 22);
export default wiz1;

