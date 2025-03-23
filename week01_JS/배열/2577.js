const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split('\n');

// 구조 분해 할당으로 A, B, C 
let [A, B, C] = input.map(Number)

//  모두 곱한 값을 문자열로 변경후, split 메서드 써서 리스트 화
let total = String(A * B * C).split('')


let int_list = []
// 각 문자열 원소를 다시 숫자형 원소로 변경
total.forEach(element => {
  int_list.push(parseInt(element))
});

// 숫자 개수를 담을 리스트 생성
answer_array = new Array(10).fill(0)

// 한 글자씩 돌면서 해당 숫자 인덱스에 1 추가
for (let char of int_list) {
  answer_array[char] += 1
}

console.log(answer_array.join('\n'))

