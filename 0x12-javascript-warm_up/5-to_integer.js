#!/usr/bin/node

const myArr = process.argv;
const myRex = parseInt(myArr[2]);

if (Number.isInteger(myRex)) {
  console.log('My number: ' + parseInt(myArr[2]));
} else {
  console.log('Not a number');
}
