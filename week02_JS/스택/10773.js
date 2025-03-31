// 0을 만나면 바로 전 쓴 수를 pop

const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

let N = parseInt(input[0])
let wallet = []

for (let i = 1; i <= N; i++) {
  number = parseInt(input[i])
  if (number == 0) {
    wallet.pop()
  } else {
    wallet.push(number)
  }
}

// TypeError: Reduce of empty array with no initial value
if (wallet.length == 0) {
  console.log(0)
} else {
  console.log(wallet.reduce((prev, cur) => prev + cur))
}
