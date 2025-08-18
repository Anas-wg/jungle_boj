const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let [N, M] = input[0].split(' ').map(Number);
let graph = [];
for (let i = 1; i <= N; i++) {
  graph.push(input[i].split('').map(Number));
}

let dx = [0, 0, -1, 1];
let dy = [-1, 1, 0, 0];

const BFS = (x, y) => {
  let queue = [];
  queue.push([x, y, 1]); // [x, y, 거리]를 함께 저장
  graph[x][y] = 0; // 방문한 곳은 0으로 표시 (visited 배열 대신 사용)

  while (queue.length > 0) {
    let [currX, currY, dist] = queue.shift();

    // BFS 이므로 자연스럽게 최단 경로일때 도달함
    if (currX === N - 1 && currY === M - 1) {
      return dist;
    }

    for (let i = 0; i < 4; i++) {
      let nx = currX + dx[i];
      let ny = currY + dy[i];

      if (nx >= 0 && nx < N && ny >= 0 && ny < M && graph[nx][ny] === 1) {
        queue.push([nx, ny, dist + 1]); // 이동 가능하니 거리 1 추가
        graph[nx][ny] = 0;
      }
    }
  }
  return -1; // 경로를 찾지 못했을 경우
};

console.log(BFS(0, 0));