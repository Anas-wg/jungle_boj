const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let N = parseInt(input[0])
let seq = input[1].split(' ').map(Number);

let result = [];
for (let i = 0; i < N; i++) {
  let a_i = seq[i];
  let seq_right = seq.slice(i + 1,).filter((elem) => elem > a_i);
  // console.log(seq_right);
  // let seq_right = [...seq].filter((elem) => elem > a_i);

  if (seq_right.length == 0) {
    result.push(-1);
    continue;
  }

  seq_right.sort((a, b) => a - b);

  if (a_i < seq_right[0]) {
    result.push(seq_right[0]);
  } else {
    result.push(-1)
  }
}

console.log(result.join(' '))

