// M개의 정수가 N개의 정수 리스트 안에 있는지 확인

const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0]);
let A_list = input[1].split(' ').map(Number)
let M = parseInt(input[2])
let M_list = input[3].split(' ').map(Number)

let result = []

// N개의 정수 정렬
A_list.sort((a, b) => a - b)
console.log(A_list)
// 이분 탐색
function binary_search(arr, target) {
  let start = 0
  let end = arr.length - 1

  while (start <= end) {
    let mid = Math.ceil((start + end) / 2)
    if (arr[mid] == target) {
      result.push(1)
      return
    } else if (arr[mid] > target) {
      end = mid - 1
    } else {
      start = mid + 1
    }
  }
  result.push(0)
  return
}

M_list.forEach(elems => binary_search(A_list, elems))
console.log(result.join('\n'))