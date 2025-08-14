const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0])
let plan = input[1].split(' ')

let cur_x = 1
let cur_y = 1

let dx = [0, 0, -1, 1]
let dy = [-1, 1, 0, 0]
let moves = ['L', 'R', 'U', 'D'];

for (let i = 0; i < plan.length; i++) {
  let move = plan[i];
  let nx = cur_x
  let ny = cur_y
  // nx, ny 계산
  for (let j = 0; j < move.length; j++) {
    if (move === moves[j]) {
      nx += dx[j]
      ny += dy[j]
      break;
    }
  }
  // N의 범위 내인지 체크, 범위 내라면 적용
  if (nx >= 1 && nx <= N && ny >= 1 && ny <= N) {
    cur_x = nx;
    cur_y = ny;
  }

}

// plan.forEach((elem) => {
//   console.log(elem)
//   console.log(cur_x, cur_y)
//   if (elem == 'U') {
//     new_x = cur_x - 1
//     if (new_x > 0) {
//       cur_x = new_x
//     }
//   } else if (elem == 'D') {
//     new_x = cur_x + 1
//     if (new_x <= N) {
//       cur_x = new_x
//     }
//   } else if (elem == 'L') {
//     new_y = cur_y - 1
//     if (new_y > 0) {
//       cur_y = new_y
//     }
//   } else {
//     new_y = cur_y + 1
//     if (new_y <= N) {
//       cur_y = new_y
//     }
//   }
// })

// console.log(cur_x, cur_y)
