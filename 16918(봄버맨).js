const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');

let [R, C, N] = input[0].split(' ').map(Number);

let map = []
for (let i = 1; i <= R; i++) {
  map.push(input[i].split(''))
}
let seconds = 1;
let dx = [0, 0, -1, 1]
let dy = [-1, 1, 0, 0]

while (true) {
  let initialBomb = []
  // O 좌표 기억
  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (map[i][j] === 'O') {
        initialBomb.push([i, j])
      }
    }
  }

  if (seconds === N) {
    break;
  } else {
    seconds += 1
  }

  // 전부 O로 채우기
  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      map[i][j] = 'O'
    }
  }


  if (seconds === N) {
    break;
  } else {
    seconds += 1
  }


  // 4방향 폭파
  initialBomb.forEach((elem) => {
    const [bombRow, bombCol] = elem;
    map[bombRow][bombCol] = '.';

    for (let k = 0; k < 4; k++) {
      const ny = bombRow + dy[k];
      const nx = bombCol + dx[k];

      if (ny >= 0 && ny < R && nx >= 0 && nx < C) {
        map[ny][nx] = '.';
      }
    }
  });

}


for (let i = 0; i < R; i++) {
  console.log(map[i].join(''))
}
