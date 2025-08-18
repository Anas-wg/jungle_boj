const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0]);
let array = []

for (let i = 1; i <= N; i++) {
  array.push(parseInt(input[i]))
}

array.sort((a, b) => b - a)

console.log(array.join(' '))

