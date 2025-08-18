const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0]);
let array = []

for (let i = 1; i <= N; i++) {
  let [name, score] = input[i].split(' ')
  array.push([name, parseInt(score)])
}

array.sort((a, b) => a[1] - b[1])

let result = []

array.forEach((elem) => result.push(elem[0]))

console.log(result.join(' '))