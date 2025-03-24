// 완전탐색, 조합...말고 9명의 키의 합에서 2명의 키를 빼는데 그 두명을 완전탐색

const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let smalls_list = []
for (let i = 0; i < 9; i++) {
  smalls_list.push(parseInt(input[i]))
}

total_height = smalls_list.reduce((prev, cur) => prev + cur)
let found = false;


for (let i = 0; i < 8; i++) {
  for (let j = i + 1; j < 9; j++) {
    if (total_height - (smalls_list[i] + smalls_list[j]) == 100) {

      smalls_list.splice(j, 1);  // index j 를 먼저 제거
      smalls_list.splice(i, 1);  // index i 를 제거 (j가 제거된 후의 위치)
      // smalls_list = smalls_list.filter((el) => el !== smalls_list[i])
      // smalls_list = smalls_list.filter((el) => el !== smalls_list[j])
      found = true;
      break
    }
  }
  if (found) break;
}
smalls_list.sort((a, b) => a - b)
console.log(smalls_list.join('\n'))