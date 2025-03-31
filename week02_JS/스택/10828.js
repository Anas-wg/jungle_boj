// JS로 스택 구현
const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0])
let stack = []
let result = []


for (let i = 1; i <= N; i++) {
  let [order, num] = input[i].split(' ')
  if (order == 'push') {
    push(parseInt(num))
  } else if (order == 'pop') {
    pop()
  } else if (order == 'size') {
    size()
  } else if (order == 'empty') {
    empty()
  } else if (order == 'top') {
    top()
  }
}


function push(N) {
  stack.push(N)
}

function pop() {
  if (stack.length == 0) {
    result.push(-1)
  } else {
    result.push(stack.pop())
  }
}

function size() {
  result.push(stack.length)
}

function empty() {
  if (stack.length == 0) {
    result.push(1)
  } else {
    result.push(0)
  }
}

function top() {
  if (stack.length == 0) {
    result.push(-1)
  } else {
    result.push(stack[stack.length - 1])
  }
}

console.log(result.join('\n'))