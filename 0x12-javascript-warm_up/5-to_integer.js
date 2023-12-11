#!/usr/bin/node
const myString = process.argv[2];
const myNum = parseInt(myString);
if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
