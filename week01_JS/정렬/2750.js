// N개의 수가 주어졌을때 이를 오름차순 정렬
const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

let N = parseInt(input[0])
let num_list = []

for (let i = 1; i <= N; i++) {
  num_list.push(parseInt(input[i]))
}

// console.log(num_list.sort().join('\n'))
num_list.sort((a, b) => a - b)
console.log(num_list.join('\n'))