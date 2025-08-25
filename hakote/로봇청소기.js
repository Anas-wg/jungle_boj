const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [N, M] = input[0].split(' ').map(Number)
let [x, y, d] = input[1].split(' ').map(Number)

let graph = []

for (let i = 2; i < 2 + N; i++) {
  graph.push(input[i].split(' ').map(Number))
}

// 북 동 남 서 
let dx = [0, 1, 0, -1]
let dy = [-1, 0, 1, 0]

// 회전 함수화

const rotate = () => {
  d = d - 1
  if (d === -1) {
    d = 3
  }
}

let visited = Array.from({ length: N }, () => Array(M).fill(false))
let step = 0
// 이동

while (true) {
  let turn_time = 0
  if (!visited[x][y]) {
    step += 1
  }
  visited[x][y] = true
  // 4방향 체크
  for (let i = 0; i < 4; i++) {
    nx = x + dx[i]
    ny = y + dy[i]
    // 청소되지 않은 빈칸 있다면
    if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && graph[nx][ny] !== 1) {
      rotate() // 90도 회전
      next_x = x + dx[d]
      next_y = y + dx[d]
      if (!visited[next_x][next_y]) {
        x = next_x
        y = next_y
        graph[nx][ny] = 2
      }
      break
    }
  }
  // 청소되지 않은 빈칸이 없는 경우
  nx = x - dx[d]
  ny = y - dx[d]
  if (nx >= 0 && nx < N && ny >= 0 && ny < M && graph[nx][ny] !== 1) {
    x = nx
    y = ny
  } else {
    break
  }
}

console.log(step)

