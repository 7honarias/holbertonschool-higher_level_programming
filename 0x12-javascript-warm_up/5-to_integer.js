#!/usr/bin/node

const myArr = process.argv;
const myRex = parseInt(myArr[2]);

if (Number.isInteger(myRex)) {
  console.log(parseInt(myArr[2]));
} else {
  console.log('Not a number');
}
