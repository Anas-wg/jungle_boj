const fs = require("fs")
const input = fs.readFileSync('input.txt').toString().trim().split("\n").map(Number)


max_val = Math.max(...input)
console.log(max_val)
console.log(input.indexOf(max_val) + 1)
