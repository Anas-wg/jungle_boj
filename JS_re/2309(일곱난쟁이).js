const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');

// 일곱 난쟁이의 합이 100
// 완전탐색 -> 2명을 고르는 픽을 완전탐색으로

let N = 9;
let smalls = [];
for (let i = 0; i < N; i++) {
  smalls.push(parseInt(input[i]));
}

let total_sum = smalls.reduce((acc, num) => acc + num);
let found = false;

for (let i = 0; i < N; i++) {
  for (let j = i + 1; j < N; j++) {
    let two_sum = smalls[i] + smalls[j];
    if (total_sum - two_sum == 100) {
      smalls.splice(j, 1);
      smalls.splice(i, 1);
      break;
    }
  }
  if (smalls.length == 7) break;
}

smalls.sort((a, b) => a - b)
console.log(smalls.join('\n'));