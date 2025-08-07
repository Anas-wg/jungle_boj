const fs = require('fs');
let [N, K] = fs.readFileSync('input.txt').toString().trim().split(' ').map(Number);

let answer = 0

while (N !== 1) {
  if (N % K === 0) {
    N = N / K
    answer += 1
  } else {
    N -= 1
    answer += 1
  }

}

console.log(answer)

