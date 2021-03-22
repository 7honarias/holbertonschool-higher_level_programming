#!/usr/bin/node

const myArr = process.argv;
if (myArr[2] === undefined) {
  console.log('No argument');
} else {
  console.log(myArr[2]);
}
