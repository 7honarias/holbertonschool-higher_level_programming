#!/usr/bin/node

function Factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  return n * Factorial(n - 1);
}
const num = parseInt(process.argv[2]);
if (Number.isInteger(num)) {
  console.log(Factorial(num));
} else {
  console.log(1);
}
