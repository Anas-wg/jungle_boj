const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let [N, M, K] = input[0].split(' ').map(Number);
let array = input[1].split(' ').map(Number);

array.sort((a, b) => b - a)


// 가장 큰 수를 K번 더하기
// M이 남았다면 
// 그 다음 큰수 1번 더하기
let answer = 0

while (true) {
  for (let i = 0; i < K; i++) {
    if (M === 0) {
      break
    }
    answer += array[0]
    M -= 1
  }
  if (M === 0) {
    break
  }
  answer += array[1]
  M -= 1
}

console.log(answer)