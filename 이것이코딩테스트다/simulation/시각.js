const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim();

let N = parseInt(input[0])

let answer = 0;

for (let h = 0; h <= N; h++) {
  for (let m = 0; m <= 59; m++) {
    for (let s = 0; s <= 59; s++) {
      let time = `${h},${m},${s}`
      if (time.includes('3')) {
        answer += 1
      }
    }
  }
}

console.log(answer)