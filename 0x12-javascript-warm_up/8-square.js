#!/usr/bin/node

const numberOfSize = Number(process.argv[2]);

if (isNaN(numberOfSize)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < numberOfSize; index++) {
    console.log('X'.repeat(numberOfSize));
  }
}
