#!/usr/bin/node
const fs = require('fs');
const path = require('path');

function concatenateFiles (sourceFilePath1, sourceFilePath2, destinationFilePath) {
  try {
    const data1 = fs.readFileSync(sourceFilePath1, 'utf8');
    const data2 = fs.readFileSync(sourceFilePath2, 'utf8');
    const concatenatedData = data1 + data2;
    fs.writeFileSync(destinationFilePath, concatenatedData, 'utf8');
    console.log(`${concatenatedData}`);
  } catch (err) {
    console.error('Error:', err.message);
  }
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: node concatFiles.js sourceFile1.txt sourceFile2.txt destinationFile.txt');
} else {
  concatenateFiles(sourceFile1, sourceFile2, destinationFile);
}
