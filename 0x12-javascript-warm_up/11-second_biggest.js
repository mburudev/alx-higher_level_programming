#!/usr/bin/node
function findSecondBiggest (numbers) {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  const uniqueNumbers = [...new Set(sortedNumbers)];

  if (uniqueNumbers.length < 2) {
    return 0;
  }

  return uniqueNumbers[1];
}

const args = process.argv.slice(2).map(arg => parseInt(arg, 10));
const integerArgs = args.filter(arg => !isNaN(arg) && Number.isInteger(arg));

if (integerArgs.length < 2) {
  console.log(0);
} else {
  const secondBiggest = findSecondBiggest(integerArgs);
  console.log(secondBiggest);
}
