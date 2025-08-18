const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let [N, K] = input[0].split(' ').map(Number)
let arrayA = input[1].split(' ').map(Number)
let arrayB = input[2].split(' ').map(Number)

arrayA.sort((a, b) => a - b)
arrayB.sort((a, b) => b - a)

for (let i = 0; i < K; i++) {
  arrayA[i] = arrayB[i]
}

console.log(arrayA.reduce((prev, cur) => prev + cur))