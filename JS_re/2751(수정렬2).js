const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');

let N = parseInt(input[0]);
let num_list = [];
for (let i = 1; i <= N; i++) {
  num_list.push(parseInt(input[i]));
}

function merge_sort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const low_arr = merge_sort(arr.slice(0, mid));
  const high_arr = merge_sort(arr.slice(mid));

  let merged_arr = [];
  let l = 0, h = 0;

  while (l < low_arr.length && h < high_arr.length) {
    if (low_arr[l] < high_arr[h]) {
      merged_arr.push(low_arr[l]);
      l += 1;
    } else {
      merged_arr.push(high_arr[h]);
      h += 1;
    }
  }

  // 남은 요소들 추가
  merged_arr = merged_arr.concat(low_arr.slice(l));
  merged_arr = merged_arr.concat(high_arr.slice(h));

  return merged_arr;
}

const sorted_list = merge_sort(num_list);
console.log(sorted_list.join('\n'));