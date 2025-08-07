let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 테스트케이스 개수
let testCase = Number(input[0]);
// 출력할 결과
let answer = "";

function backtrack(n, depth, result, operators, numbers) {
  if (depth == n - 1) {
    let calculate = "";
    for (let r = 0; r < result.length; r++) {
      if (result[r] != " ") calculate += result[r];
    }
    if (eval(calculate) == 0) answer += result.join("") + '\n';
    return;
  }

  // Operators([" ", "+", "-"] 순회)
  for (let i = 0; i < 3; i++) {
    result.push(operators[i]);
    if (depth != n - 1) result.push(numbers[depth + 1]);
    backtrack(n, depth + 1, result, operators, numbers);
    result.pop();
    result.pop();
  }
}

// 테스트케이스 순회
for (let t = 1; t <= testCase; t++) {
  // 1부터 n까지 들어있는 배열
  let n = Number(input[t]);
  let numbers = Array.from({ length: n }, (v, i) => i + 1)

  // ASCII 순서에 따라 연산자 배치 
  // (charCodeAt으로 확인하면 32, 43, 45)
  let operators = [" ", "+", "-"]
  let result = [numbers[0]];

  backtrack(n, 0, result, operators, numbers);
  answer += '\n';
}
console.log(answer)