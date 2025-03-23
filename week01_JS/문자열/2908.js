//  숫자를 뒤집어서 크기 비교

const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split(' ')
let A = input[0]
let B = input[1]
// 문자열 -> 리스트, 리스트 뒤집기

A = A.split('').reverse()
B = B.split('').reverse()

A = parseInt(A.join(''))
B = parseInt(B.join(''))

console.log(A > B ? A : B)