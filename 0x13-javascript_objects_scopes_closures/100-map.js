#!/usr/bin/node
const myArr = require('./100-data').list;

const newArr = myArr.map(function (x, index) {
  return x * index;
});
console.log(myArr);
console.log(newArr);
