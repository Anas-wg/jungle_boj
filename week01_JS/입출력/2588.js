const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

let first = parseInt(input[0])
let second = parseInt(input[1])
let second_digit = [...input[1]]

console.log(first * parseInt(second_digit.at(-1)))
console.log(first * parseInt(second_digit.at(-2)))
console.log(first * parseInt(second_digit.at(-3)))
console.log(first * second)