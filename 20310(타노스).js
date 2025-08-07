const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim()

// 구할 것 : 짝수개의 0, 짝수개의 1로 구성된 문자열 S 중 0과 1 절반씩을 제거한 뒤 사전순으로 가장 빠른 S` 구하기.
// 어떻게 절반을 날릴 것인가? => 0과 1의 개수를 Count, 절반씩 날릴 수 있는 Case를 완전탐색?, 자릿수도 절반이 줄어든다.

// 1. 문자열의 0과 1의 개수를 파악
// 2. 가장 사전순으로 앞선 순서 => 0이 1보다 앞에 있어야함
// 3. 앞에서 부터 위치한 1을 지우기?
// 4. 0은 뒤에서 부터 지워서 1을 가장 뒤에 위치. (101 이 아니 011 로)

let S = [...input];
let z_count = 0;
let o_count = 0;

S.forEach(element => {
  if (element == "0") {
    z_count += 1;
  } else {
    o_count += 1;
  }
});


let ones_to_remove = o_count / 2;
let ones_removed_count = 0;
for (let i = 0; i < S.length; i++) {
  if (ones_removed_count >= ones_to_remove) {
    break;
  }
  if (S[i] == "1") {
    S.splice(i, 1);
    ones_removed_count++;
    i--;
  }
}

console.log(S);

let zeros_to_remove = z_count / 2;
let zeros_removed_count = 0;
for (let i = S.length - 1; i >= 0; i--) {
  if (zeros_removed_count >= zeros_to_remove) {
    break;
  }
  if (S[i] == "0") {
    S.splice(i, 1);
    zeros_removed_count++;
  }
}

console.log(S.join(''));
