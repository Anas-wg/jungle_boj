// X의 각 자리가 등차수열인 수
// 1보다 크거나 같고 N작거나 같음 수
const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim();

let N = parseInt(input)

function is_hansu(num_digits) {
  if (num_digits.length == 1) {
    return true
  }
  else if (num_digits.length == 2) {
    return true
  }
  else {
    if (num_digits[0] - num_digits[1] == num_digits[1] - num_digits[2]) {
      return true
    }
  }
  return false
}

let answer = 0

for (let i = 1; i <= N; i++) {
  i_digits = String(i).split('').map(Number)
  if (is_hansu(i_digits)) {
    answer += 1
  }
}

console.log(answer)

