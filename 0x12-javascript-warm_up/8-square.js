#!/usr/bin/node

const arg = process.argv[2];
const numArg = Number(arg);

if (isNaN(numArg)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < numArg; a++) {
    let output = '';
    for (let i = 0; i < numArg; i++) {
      output += 'x';
    }
    console.log(output);
  }
}
