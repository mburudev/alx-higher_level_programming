#!/usr/bin/node
const { dict } = require('./101-data.js');

function invertDictionary (inputDict) {
  const resultDict = {};

  for (const userId in inputDict) {
    const occurrences = inputDict[userId];

    if (!resultDict[occurrences]) {
      resultDict[occurrences] = [];
    }

    resultDict[occurrences].push(userId);
  }

  return resultDict;
}

const invertedDict = invertDictionary(dict);

console.log(invertedDict);
