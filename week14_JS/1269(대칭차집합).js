const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [leng_A, leng_B] = input[0].split(' ').map(Number);
const A = input[1].split(' ').map(Number);
const B = input[2].split(' ').map(Number);

const setA = new Set(A);
const setB = new Set(B);

let count = 0;

for (const elem of setA) {
  if (!setB.has(elem)) {
    count++;
  }
}

for (const elem of setB) {
  if (!setA.has(elem)) {
    count++;
  }
}

console.log(count);