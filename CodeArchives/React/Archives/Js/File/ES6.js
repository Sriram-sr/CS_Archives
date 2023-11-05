class checker {
    constructor(){
        console.log('Instance is created');
        console.log(this);
    }
}

// function checkFunction(){
//     console.log(this);
// }
const checkFunction = () => {
    console.log(this);
}

checkFunction();

const args = {
    name: 'Sr',
    age: 22,
    place: {
        old: 'pvm',
        new: 'spt'
    }
};

const argsFunct = ({name, place: { new } }) =>{
    console.log(`Ive got arguments as ${name} and ${place}`);
}

argsFunct(args);