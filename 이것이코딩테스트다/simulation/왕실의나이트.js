const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim();

let col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
let [cur_col, cur_row] = input.split('')
let answer = 0;

cur_row = parseInt(cur_row);
cur_col = col.indexOf(cur_col) + 1


let dx = [-1, 1, -2, 2, 2, -2, -1, 1]
let dy = [-2, 2, -1, 1, -1, 1, 2, -2]

for (let i = 0; i < 8; i++) {
  let nx = cur_col + dx[i]
  let ny = cur_row + dy[i]
  if (nx > 0 && nx <= 8 && ny > 0 && ny <= 8) {
    answer += 1
  }
}

console.log(answer)
