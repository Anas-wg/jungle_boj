const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

// 골드바흐 파티션 => 2로 나눈 수 부터 확인,(뒤에서 앞으로)
// 14 라면 1~ 7 까지 리스트를 생성 => 7과 14 -7을 확인
// 소수가 아니라면 그 앞의 수

let T = parseInt(input[0])

function is_sosu(number) {
  if (number == 1) {
    return false
  }
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i == 0) {
      return false
    }
  }
  return true
}

for (let i = 1; i <= T; i++) {
  let N = parseInt(input[i] / 2)
  arr = []
  for (let i = 1; i <= N; i++) {
    arr.push(i)
  }
  arr.reverse()
  for (let nums of arr) {
    if (is_sosu(nums) && is_sosu(input[i] - nums)) {
      console.log(nums, input[i] - nums)
    }
  }

}