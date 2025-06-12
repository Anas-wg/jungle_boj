// 이분탐색
// N = 나무 수, M = 가져가려고하는 나무 길이
// ANS. M 미터 나무를 가져기위한 절단기 높이의 최댓값
// 1. 입력받기
const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\n');
let [N, M] = input[0].split(' ').map(Number);
let trees = input[1].split(' ').map(Number);

// 2. 나무 정렬
trees.sort((prev, curr) => prev - curr);
console.log(trees);
// 3. 높이 가운데 값 부터 가져가려고 하는 나무 길이를 충족하는지 체크
// 만약 가운데 값으로 잘랐을때 합이, M 보다 작다면 높이를 낮추어야함.
let start = Math.floor((trees[0] + trees[trees.length - 1]) / 2);
let result = 0;

while (M != result) {
  for (i = 0; i < N; i++) {
    if (trees[i] < start) {
      continue
    } else {
      result += (trees[i] - start);
    }
  }
}


