#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
