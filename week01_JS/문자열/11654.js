// 아스키 코드 출력

const fs = require("fs")
const input = fs.readFileSync('input.txt').toString().trim()

console.log(input.charCodeAt())