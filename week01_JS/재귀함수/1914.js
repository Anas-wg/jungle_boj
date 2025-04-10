// 하노이탑
// hanoi(3) => 2개의 원판 A -> B (C 경유)
// 3번째 원판 A -> C 
// 나머지 2개의 원판 B -> C (A 경유)

const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim()

let N = parseInt(input)

// console.log는 시간 초과가 날 수 있다
let result = []; // 결과 출력용 배열

function hanoi(N, start, end, sub) {
  if (N == 1) {
    result.push(`${start} ${end}`)
  } else {
    hanoi(N - 1, start, sub, end)
    result.push(`${start} ${end}`)
    hanoi(N - 1, sub, end, start)
  }
}

console.log((BigInt(2) ** BigInt(N) - BigInt(1)).toString());

if (N <= 20) {
  hanoi(N, 1, 3, 2);
  console.log(result.join('\n'))
}