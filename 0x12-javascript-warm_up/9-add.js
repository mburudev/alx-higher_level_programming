#!/usr/bin/node
function add (a, b) {
  const result = a + b;
  console.log(`${result}`);
}

const num1 = process.argv[2];
const num2 = process.argv[3];

if (num1 && num2 !== undefined) {
  add(Number(num1), Number(num2));
} else {
  console.log('NaN');
}
