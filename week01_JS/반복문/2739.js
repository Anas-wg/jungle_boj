// 구구단 출력
const fs = require("fs")
const input = fs.readFileSync("input.txt").toString().trim()

N = parseInt(input)

for (let i = 1; i <= 9; i++) {
  console.log(`${N} * ${i} = ${N * i}`)
}