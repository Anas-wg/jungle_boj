// 배열의 순서를 적절히 변경하여 수식의 결과값을 최대로

const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

// 순열을 구현하고 각각 순열의 합 중 최대 합을 리턴

let N = parseInt(input[0])
let num_list = input[1].split(' ').map(Number)


const getPerm = (arr, n) => {
  if (n == 1) return arr.map(el => [el]);
  const result = [];

  arr.forEach((fixed, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)]
    const perms = getPerm(rest, n - 1)
    const attached = perms.map(perm => [fixed, ...perm])
    result.push(...attached)
  });
  return result
}

perm_list = getPerm(num_list, N)
result_list = []

for (let perm of perm_list) {
  let result = 0
  for (let i = 1; i < perm.length; i++) {

    result += Math.abs(perm[i] - perm[i - 1])
  }
  result_list.push(result)
}

console.log(Math.max(...result_list))