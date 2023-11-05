const file_system = require('fs');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
const view_users = (data) => {
    for (const user in data){
        console.log(data[user]['Cus_Name']);
    }
}

const check_bank_balance = () => {

}

const json_text = JSON.parse(file_system.readFileSync('server_entries.json'));
// view_users(json_text);


// Importing the module
const readline = require("readline-sync");
  
// Enter the number
let a = Number(readline.question());
console.log(a);
let number = [];
  