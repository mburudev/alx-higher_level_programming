#!/usr/bin/node

const arg = process.argv[2];
const numArg = Number(arg);

if (isNaN(numArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numArg}`);
}
