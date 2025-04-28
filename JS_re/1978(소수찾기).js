const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().split('\n');

// 1. 입력받기
let N = parseInt(input[0]);
let arr = input[1].split(' ').map(Number);
let answer = 0;
// 2. 소수 판별 함수

function is_sosu(num) {
  let is_sqrt = true;
  if (num == 1) {
    is_sqrt = false;
    return;
  }

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i == 0) {
      is_sqrt = false;
      break;
    }
  }
  if (is_sqrt) {
    answer++;
  }
}


arr.forEach(num => is_sosu(num));

console.log(answer);


