#!/usr/bin/node
// reads and prints the content of a file passed as an argument

const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});
