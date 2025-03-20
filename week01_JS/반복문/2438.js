const fs = require("fs")
input = fs.readFileSync("input.txt").toString().trim()

let N = parseInt(input)
for (let i = 1; i <= N; i++) {
  console.log("*".repeat(i))
}