const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const [[N], ...Board] = fs.readFileSync(path).toString().trim().split('\n').map(row => row.split(' ').map(Number));

// 1. 이동 가능한 경우의 수

let dx = [0, 0, -1, 1]
let dy = [-1, 1, 0, 0]


