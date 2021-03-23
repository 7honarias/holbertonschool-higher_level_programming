#!/usr/bin/node

const myDict = require('./101-data').dict;
const newDict = {};

for (const key in myDict) {
  const val = myDict[key];
  if (Object.prototype.hasOwnProperty.call(newDict, val)) {
    const arr = newDict[val];
    arr.push(key);
    newDict[val] = arr;
  } else {
    const arr = [key];
    newDict[val] = arr;
  }
}
console.log(newDict);
