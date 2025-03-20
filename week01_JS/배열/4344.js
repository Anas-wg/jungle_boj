const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split('\n');

let C = parseInt(input[0])
for (let i = 1; i <= C; i++) {
  let arr = input[i].split(" ").map(Number)
  let student_pax = arr[0]
  let total_score = arr.reduce((prev, cur) => prev + cur, 0) - student_pax
  let avg = total_score / student_pax
  let upper_avg = 0
  for (let i = 1; i <= arr.length; i++) {
    if (arr[i] > avg) {
      upper_avg += 1
    }
  }
  console.log(`${((upper_avg / student_pax) * 100).toFixed(3)}%`)
}