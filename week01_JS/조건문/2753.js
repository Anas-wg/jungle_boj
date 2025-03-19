
// 윤년 => 4의 배수 이면서 100의 배수가 아닌 것 || 400의 배수
const fs = require("fs")
const input = fs.readFileSync('input.txt').toString().trim()

year = parseInt(input)

if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
  console.log(1)
} else {
  console.log(0)
}