// 뭘 분할 할까?
// 1. 입력받기
// 2. N * N 안에 다 동일한 숫자라면 숫자에 맞는 사각형 변수 ++
// 3. 만약 다른 숫자라면 N/2 * N/2로 분할.
const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0])
const paper = Array.from({ length: N }, (_, i) => input[i + 1].split(' ').map(Number))

// paper = []
// for (let i = 1; i <= N; i++) {
//   paper.push(input[i].split(' ').map(Number))
// }

let result = []

function solution(a, b, N) {
  let color = paper[a][b]
  for (let i = a; i < a + N; i++) {
    for (let j = b; j < b + N; j++) {
      if (color != paper[i][j]) {
        let range = Math.floor(N / 2)
        solution(a, b, range)
        solution(a, b + range, range)
        solution(a + range, b, range)
        solution(a + range, b + range, range)
        return
      }
    }
  }
  if (color == 0) {
    result.push(0)
  } else {
    result.push(1)
  }
}

solution(0, 0, N)
console.log(result.filter(elem => elem == 0).length)
console.log(result.filter(elem => elem == 1).length)