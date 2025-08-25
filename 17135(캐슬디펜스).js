const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const [[N, M, D], ...initialBoard] = fs.readFileSync(path).toString().trim().split('\n').map(row => row.split(' ').map(Number));

// M개의 열 중 3개의 궁수를 배치할 수 있는 모든 조합을 구하는 함수
const putArchery = () => {
  const locations = [];
  for (let i = 0; i < M - 2; i++) {
    for (let j = i + 1; j < M - 1; j++) {
      for (let k = j + 1; k < M; k++) {
        // [열1, 열2, 열3] 형태로 조합을 저장
        locations.push([i, j, k]);
      }
    }
  }
  return locations;
};

// 두 위치 (r1, c1)와 (r2, c2) 사이의 맨해튼 거리를 계산하는 함수
const calculateDistance = ([r1, c1], [r2, c2]) => {
  return Math.abs(r1 - r2) + Math.abs(c1 - c2);
};

const solve = () => {
  let maxKilled = 0; // 게임에서 최대로 잡을 수 있는 적의 수
  const archerLocations = putArchery(); // 궁수 배치 조합 배열

  // 모든 궁수 배치 조합에 대해 게임을 시뮬레이션
  for (const archers of archerLocations) {
    // 시뮬레이션을 위해 초기 보드를 깊게 복사
    const board = initialBoard.map(row => [...row]);
    let killedThisGame = 0; // 현재 시뮬레이션에서 잡은 적의 수

    // N번의 턴 동안 시뮬레이션 진행
    for (let turn = 0; turn < N; turn++) {
      // 3명의 궁수가 공격할 타겟을 저장할 배열
      const targets = [];

      // 각 궁수가 공격할 적을 찾음
      for (const archerCol of archers) {
        let target = null;
        let minDist = Infinity; // 최소 거리
        let minCol = Infinity; // 최소 거리가 같을 때 가장 왼쪽 열

        // 적을 찾기 위해 보드 전체를 탐색 (맨 아래 행부터 위로)
        for (let i = N - 1; i >= 0; i--) {
          for (let j = 0; j < M; j++) {
            if (board[i][j] === 1) { // 적이 있는 칸이면
              // 궁수와 적 사이의 거리 계산 (궁수는 N행 바로 아래, N+1행에 위치)
              const dist = calculateDistance([N, archerCol], [i, j]);

              if (dist <= D) { // 사정거리 D 이내라면
                if (dist < minDist) { // 더 가까운 적을 발견하면
                  minDist = dist;
                  target = [i, j];
                  minCol = j;
                } else if (dist === minDist && j < minCol) { // 거리가 같고 더 왼쪽에 있는 적을 발견하면
                  minCol = j;
                  target = [i, j];
                }
              }
            }
          }
        }

        // 타겟이 있으면 targets 배열에 추가
        if (target) {
          // 중복 타겟인지 확인
          let isDuplicate = false;
          for (const existingTarget of targets) {
            if (existingTarget[0] === target[0] && existingTarget[1] === target[1]) {
              isDuplicate = true;
              break;
            }
          }
          if (!isDuplicate) {
            targets.push(target);
          }
        }
      }

      // 타겟으로 지정된 모든 적을 보드에서 제거하고 잡은 수 증가
      for (const [r, c] of targets) {
        if (board[r][c] === 1) {
          board[r][c] = 0;
          killedThisGame++;
        }
      }

      // 적들을 한 칸 아래로 이동
      for (let i = N - 1; i >= 0; i--) {
        for (let j = 0; j < M; j++) {
          if (board[i][j] === 1) {
            board[i][j] = 0; // 현재 위치의 적을 제거
            if (i < N - 1) {
              board[i + 1][j] = 1; // 한 칸 아래로 이동
            }
          }
        }
      }
    }
    // 현재 게임에서 잡은 적의 수가 최대값보다 크면 갱신
    maxKilled = Math.max(maxKilled, killedThisGame);
  }

  console.log(maxKilled);
};

solve();