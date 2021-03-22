#!/usr/bin/node

function add(a, b) {
  console.log(a + b);
}

const myArr = process.argv;
const num1 = parseInt(myArr[2]);
const num2 = parseInt(myArr[3]);

add(num1, num2);
