const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let [N, M] = input[0].split(' ').map(Number)

let graph = []
for (let i = 1; i <= N; i++) {
  graph.push(input[i].split('').map(Number))
}
let dx = [0, 0, 1, -1]
let dy = [-1, 1, 0, 0]

// 2. DFS 활용

let visited = Array.from({ length: N }, () => Array(M).fill(false));
let answer = 0

const dfs = (x, y) => {
  if (x < 0 || x >= N || y < 0 || y >= M || visited[x][y] || graph[x][y] === 1) {
    return
  }
  visited[x][y] = true
  dfs(x - 1, y)
  dfs(x + 1, y)
  dfs(x, y - 1)
  dfs(x, y + 1)
}

answer = 0
for (let x = 0; x < N; x++) {
  for (let y = 0; y < M; y++) {
    if (graph[x][y] == 0 && !visited[x][y]) {
      dfs(x, y)
      answer += 1
    }
  }
}

console.log(answer)