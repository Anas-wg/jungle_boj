const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split(' ')

let [A, B, V] = input.map(Number)
// 달팽이가 하루 올라갈 수 있는 거리 A - B
// 달팽이가 올라가야만 하는 거리 V -B

let result = (V - B) / (A - B)
console.log(Math.ceil(result))