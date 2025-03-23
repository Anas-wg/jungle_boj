//  주어지는 문자열은 몇개의 단어일까?
const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split(' ')

console.log(input == '' ? 0 : input.length)
