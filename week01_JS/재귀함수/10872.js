const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim()
let N = parseInt(input)

// 재귀
function factorial(N) {
  if (N == 0) {
    return 1
  } else {
    return N * factorial(N - 1)
  }
}

console.log(factorial(N))

// 반복문
function factorial_loop(N) {
  let answer = []
  number = 1
  if (N == 0) {
    return 1
  } else {
    for (let i = 1; i <= N; i++) {
      number *= i
    }
    return number
  }
}
console.log(factorial_loop(N))