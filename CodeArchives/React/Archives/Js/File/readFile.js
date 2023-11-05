var fs = require('fs');

try {  
    var data = fs.readFileSync('server_entries.json');
    const obj = JSON.parse(data);
    const userNameList = [];
    for(const user in obj){
        userNameList.push(user);
    }
    for(const name of userNameList){
        console.log(obj[name]);
    }
    const user_details = obj.User_1;
    console.log(user_details.First_Name);
} catch(e) {
    console.log('Error:', e.stack);
}