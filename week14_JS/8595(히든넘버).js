const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');

/*
  구할 것 => 단어에 숨은 숫자들의 합을 구하기
  길이가 n <= 500만...?
  연속된 숫자는 한 히든넘버
*/
// 1. 입력받기
let N = parseInt(input[0]);
let str = input[1];

// 2. str에서 어떻게 숫자를 뽑아낼까?
// 1안 -> 하나씩 체크하면서 숫자로 변경
// 2안 -> 배열에 숫자 저장
let total = 0;
let temp = "";

let str_list = [...str];
let num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

str_list.forEach((elem) => {
  if (num_list.includes(elem)) {
    temp += elem
  } else {
    if (temp !== "") {
      total += parseInt(temp);
      temp = ""
    }
  }
})

if (temp !== "") {
  total += parseInt(temp);
}
console.log(total);

