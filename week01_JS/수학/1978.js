const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0])
let num_list = input[1].split(' ').map(Number)
let answer = 0
//  소수 판독, 제곱근까지 확인 

function is_sosu(number) {
  if (number == 1) {
    return false
  }
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i == 0) {
      return false
    }
  }
  return true
}

for (let char of num_list) {
  if (is_sosu(char)) {
    answer += 1
  }
}

console.log(answer)