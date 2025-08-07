const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [W_length, S_length] = input[0].split(' ').map(Number)
let W = input[1].split('')
let maya_S = input[2];
let answer = 0;

for (let i = 0; i <= S_length - W_length; i++) {
  let s_splitted = maya_S.slice(i, i + W_length).split('').sort().join('');
  let w_splited = W.sort().join('')

  if (s_splitted === w_splited) {
    answer += 1
  }
}

console.log(answer)