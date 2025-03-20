const fs = require("fs")
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

T = parseInt(input[0])
for (let i = 1; i <= T; i++) {
  str = input[i].split("")
  score = 0
  o_list = []
  for (let char of str) {
    if (char === 'O') {
      o_list.push(char)
      score += o_list.length
    } else {
      o_list = []
    }
  }
  console.log(score)
}

