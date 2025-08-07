const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0])
let plan = input[1].split(' ')

let cur_x = 1
let cur_y = 1

let dx = [0, 0, -1, 1]
let dy = [-1, 1, 0, 0]

plan.forEach((elem) => {
  console.log(elem)
  console.log(cur_x, cur_y)
  if (elem == 'U') {
    new_x = cur_x - 1
    if (new_x > 0) {
      cur_x = new_x
    }
  } else if (elem == 'D') {
    new_x = cur_x + 1
    if (new_x <= N) {
      cur_x = new_x
    }
  } else if (elem == 'L') {
    new_y = cur_y - 1
    if (new_y > 0) {
      cur_y = new_y
    }
  } else {
    new_y = cur_y + 1
    if (new_y <= N) {
      cur_y = new_y
    }
  }
})

console.log(cur_x, cur_y)
