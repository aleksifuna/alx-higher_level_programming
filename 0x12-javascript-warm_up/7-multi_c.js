#!/usr/bin/node
const str = process.argv[2];
let myNum = parseInt(str);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  while (myNum > 0) {
    console.log('C is fun');
    myNum--;
  }
}
