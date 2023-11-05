const fs = require('fs');

fs.writeFile('test-file.txt', 'check for overrite', (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Written to file');
  }
});
