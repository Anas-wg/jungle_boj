//  가장 큰 종이조각 넓이
const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

let [row, col] = input[0].split(" ").map(Number)
let T = parseInt(input[1])

row_list = [0, row]
col_list = [0, col]

for (let i = 2; i < 2 + T; i++) {
  let [distance, value] = input[i].split(' ').map(Number);
  if (distance == 0) {
    col_list.push(value)
  } else {
    row_list.push(value)
  }
}

row_list.sort((a, b) => a - b)
col_list.sort((a, b) => a - b)

let answer = []

for (let i = 1; i < row_list.length; i++) {
  for (let j = 1; j < col_list.length; j++) {
    let width = row_list[i] - row_list[i - 1]
    let height = col_list[j] - col_list[j - 1]
    answer.push(width * height)
  }
}

console.log(Math.max(...answer))