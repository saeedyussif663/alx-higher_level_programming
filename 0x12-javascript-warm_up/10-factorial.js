#!/usr/bin/node

const number = Number(process.argv[2]);

function factorial (num) {
  if (isNaN(num)) return 1;

  if (num === 1 || num === 0) return 1;

  for (let index = number; index > 0; index--) {
    return num * factorial(num - 1);
  }
}

console.log(factorial(number));
