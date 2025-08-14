const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let [N, M] = input[0].split(' ').map(Number);
let [x, y, d] = input[1].split(' ').map(Number);

let arr = [];
for (let i = 2; i < N + 2; i++) {
  arr.push(input[i].split(' ').map(Number));
}

// 맵 외곽은 항상 바다이므로, 탐색 범위는 맵 전체로 해도 됨
const visited = Array.from({ length: N }, () => Array(M).fill(false));

// 북, 동, 남, 서 방향
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

let count = 1;
visited[x][y] = true;

const turnLeft = () => {
  d = d === 0 ? 3 : d - 1;
};

let turnTime = 0;
while (true) {
  turnLeft();
  turnTime++;

  let nx = x + dx[d];
  let ny = y + dy[d];

  if (!visited[nx][ny] && arr[nx][ny] === 0) {
    visited[nx][ny] = true;
    x = nx;
    y = ny;
    count++;
    turnTime = 0;
    continue;
  }

  if (turnTime === 4) {
    nx = x - dx[d];
    ny = y - dy[d];

    if (arr[nx][ny] === 0) {
      x = nx;
      y = ny;
      turnTime = 0;
    } else {
      break;
    }
  }
}

console.log(count);