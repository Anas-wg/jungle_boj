// DP? Greedy?
// 1. 입력받기
const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');

let T = parseInt(input[0]);
let answer = [];
for (let i = 1; i <= T; i++) {
  let input_num = input[i].split(' ').map(Number);
  let dist = input_num[1] - input_num[0];
  console.log(dist)
  let result = least_move(dist);
  answer.push(result);
}

// 최소 이동 경로 구하는 함수
function least_move(dist) {
  switch (dist) {
    case 0:
      return 0;
      break;
    case 1:
      return 1;
      break;
    case 2:
      return 2;
      break;
  }

  let result = 2; // 최초 이동, 마지막 이동
  dist -= 2;
  let k = 1;
  // 그리디니까 최대한 많이 이동(K + 1)
  while (true) {
    if (dist - k == 0 || dist - (k - 1) || dist - (k + 1) == 0) {
      result += 1;
      break;
    } else {
      dist -= (k + 1);
      k += 1
      result += 1
    }
  }
}


console.log(answer);