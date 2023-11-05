class AgeFinder{
    constructor(name, year){
        this.name = name;
        this.year = year;
    }

    findAge(x){
        console.log(`${this.name}, your age is ${x-this.year}`);
    }
}

let person1 = new AgeFinder('Veeramani', 1998);
let date = new Date();
let year = date.getFullYear();
person1.findAge(year);