const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

let [N, X] = input[0].split(" ").map(Number)
arr = input[1].split(" ").map(Number)

result = []

for (let elems of arr) {
  if (elems < X) {
    result.push(elems)
  }
}

console.log(result.join(' '))