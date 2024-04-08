#!/usr/bin/node

const arguments = process.argv.slice(2);
if (arguments.length === 0 || arguments.length === 1) {
  console.log(0);
  return;
}
const myArray = [];
arguments.forEach((num) => myArray.push(Number(num)));
myArray.sort();
while (myArray[myArray.length - 1] === myArray[myArray.length - 2]) {
  myArray.pop();
}
console.log(myArray[myArray.length - 2]);
