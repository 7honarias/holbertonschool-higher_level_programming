#!/usr/bin/node

let myArr = process.argv;
const myRex = /[0-9]/;
if (myRex.test(myArr[2])){
    console.log(parseInt(myArr[2]));
}else {
    console.log("Not a number");
}