// 문자열 정렬
// 길이가 짧은 순, 동일 길이라면 사전 순

const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = parseInt(input[0])
string_list = []
for (let i = 1; i <= N; i++) {
  string_list.push(input[i])
}

string_list = new Set(string_list)
string_list = [...string_list]

string_list.sort()
string_list.sort((prev, cur) => prev.length - cur.length)

console.log(string_list.join('\n'))