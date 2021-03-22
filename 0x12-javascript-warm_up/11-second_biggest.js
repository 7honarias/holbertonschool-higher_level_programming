#!/usr/bin/node

let myArr = process.argv.slice(2);
if (myArr.length <= 1) {
  console.log(0);
} else {
  myArr = myArr.map(x => parseInt(x));
  myArr.sort(function (a, b) {
    return a - b;
  });
  console.log(myArr[myArr.length - 2]);
}
