#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const myList = process.argv.slice(2).sort();
  console.log(myList.reverse()[1]);
}
