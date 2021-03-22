#!/usr/bin/node

let myArr = process.argv;
if (myArr[2] == undefined) {
    console.log("No argument");
}else {
    console.log(myArr[2]);
}