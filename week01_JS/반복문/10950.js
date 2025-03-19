const fs = require("fs")
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

const N = parseInt(input[0])

arr = input.slice(1).map(el => el.split(' ').map(Number))
console.log(arr)

for (let cases of arr) {
  let A = cases[0]
  let B = cases[1]
  console.log(A + B)
}

// arr.forEach(pair => {
//   let A = pair[0]
//   let B = pair[1]
//   console.log(A + B)
// })