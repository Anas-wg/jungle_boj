// VPS 판단
// 열린괄호 append, 닫힌괄호 pop
// 다 돌았는데 리스트에 뭔가 남아있거나, pop할때 리스트가 비어있는경우 => X

const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

let N = parseInt(input[0])

function check_VPS(string) {
  is_VPS = true
  stack = []
  string = string.split('')
  for (let char of string) {
    if (char == '(') {
      stack.push('(')
    } else {
      if (stack.length == 0) {
        is_VPS = false
        return is_VPS
      } else {
        stack.pop()
      }
    }
  }
  if (stack.length != 0) {
    is_VPS = false
  }
  return is_VPS
}

result = []
for (let i = 1; i <= N; i++) {
  string = input[i]
  if (check_VPS(string)) {
    result.push('YES')
  } else {
    result.push('NO')
  }
}

console.log(result.join('\n'))