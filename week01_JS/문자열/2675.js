//  문자열 각각의 문자를 R번 반복하고 연결
const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().trim().split('\n')

let T = input[0]
for (let i = 1; i <= T; i++) {
  let [R, S] = input[i].split(' ')
  R = Number(R)
  S = S.split('')
  answer_list = []
  S.forEach(element => {
    answer_list.push(element.repeat(R))
  });
  console.log(answer_list.join(''))
}

