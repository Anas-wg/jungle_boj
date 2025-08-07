const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let [N, M] = input[0].split(' ').map(Number);
let card = []

for (let i = 1; i <= N; i++) {
  card.push(input[i].split(' ').map(Number))
}

card = card.map((elem) => {
  return Math.min(...(elem.sort((a, b) => a - b)))
})

console.log(Math.max(...card))