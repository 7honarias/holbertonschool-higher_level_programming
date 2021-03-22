#!/usr/bin/node
const myArr = process.argv;
const size = parseInt(myArr[2]);

if (Number.isInteger(size)) {
  let str = '';

  for (let j = 0; j < size; j++) {
    str = str + 'X';
  }

  for (let i = 0; i < size; i++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
