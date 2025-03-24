const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

let N = parseInt(input[0]);
let num_list = [];

for (let i = 1; i <= N; i++) {
  num_list.push(parseInt(input[i]));
}

num_list = num_list.sort((a, b) => a - b)
console.log(num_list.join('\n'))

function merge_sort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  let mid = Math.floor(arr.length / 2);
  let low_arr = merge_sort(arr.slice(0, mid));
  let high_arr = merge_sort(arr.slice(mid));

  let merged_arr = [];
  let l = 0, h = 0;

  while (l < low_arr.length && h < high_arr.length) {
    if (low_arr[l] < high_arr[h]) {  // 수정된 부분
      merged_arr.push(low_arr[l]);
      l += 1;
    } else {
      merged_arr.push(high_arr[h]);
      h += 1;
    }
  }

  // 나머지 원소를 추가
  merged_arr = merged_arr.concat(low_arr.slice(l)).concat(high_arr.slice(h));

  return merged_arr;  // 병합 결과 반환
}

// 정렬 후 출력
console.log(merge_sort(num_list).join('\n'));
