// 나무 높이를 정렬
// 나무 높이의 중앙값 설정
// 그 높이로 자른 값과 가져가야할 높이 H를 비교
// 그 높이로 자른 값이 더 크면 => 높이가 더 높아야함
// 그 높이로 자른 값이 더 작다면 => 높이가 더 낮아야함
const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let [N, M] = input[0].split(' ').map(Number)
let tree_list = input[1].split(' ').map(Number)

tree_list.sort((a, b) => a - b)

function binary_search(arr, M) {
  let start = 0
  let end = arr[arr.length - 1]  // 나무의 최대 높이로 설정

  while (start <= end) {
    let mid = Math.floor((start + end) / 2)

    // mid 값으로 자른 나무의 길이 합을 계산
    let temp = arr.reduce((sum, height) => {
      if (height > mid) return sum + (height - mid)
      return sum
    }, 0)

    if (temp === M) {
      console.log(mid)
      return
    } else if (temp > M) {
      start = mid + 1  // 너무 많이 잘랐으니, 높이를 더 높여야 함
    } else {
      end = mid - 1    // 너무 적게 잘랐으니, 높이를 더 낮춰야 함
    }
  }

  console.log(end)
}

binary_search(tree_list, M)
