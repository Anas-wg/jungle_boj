const getPermutations = (arr) => {
  if (arr.length === 1) return [arr];
  const result = [];

  arr.forEach((fixed, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
    const perms = getPermutations(rest);
    const attached = perms.map((perm) => [fixed, ...perm]);
    result.push(...attached);
  });

  return result;
};

// 1. 입력받기
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
const cities = [];
for (let i = 1; i <= N; i++) {
  cities.push(input[i].split(' ').map(Number));
}

// 2. 모든 경로의 순열 생성
const permut = getPermutations(Array.from({ length: N - 1 }, (_, i) => i + 1));

// 3. 최소값 할당할 변수 선언
let minCost = Infinity;

// 4. 순열 순회하며 비용 계산
for (const perm of permut) {
  let totalCost = 0;
  let valid = true;
  let start = 0;

  for (const nextCity of perm) {
    if (cities[start][nextCity] === 0) {
      valid = false;
      break;
    }
    totalCost += cities[start][nextCity];
    start = nextCity;
  }

  // 순회가 유효하고, 마지막 도시에서 출발지로 돌아오는 비용이 존재하는 경우
  if (valid && cities[start][0] !== 0) {
    totalCost += cities[start][0];
    minCost = Math.min(minCost, totalCost);
  }
}

console.log(minCost);
