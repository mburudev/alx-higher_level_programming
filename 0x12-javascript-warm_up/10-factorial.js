#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * computeFactorial(n - 1);
}

const arg = process.argv[2];
const n = parseInt(arg);

if (!isNaN(n) && Number.isInteger(n)) {
  const factorial = computeFactorial(n);
  console.log(`${factorial}`);
} else {
  console.log('1');
}
