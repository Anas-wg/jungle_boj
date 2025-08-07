let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n');

// let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const printer = (list) => {
  let result = []

  while (list.length > 0) {
    let docs = list.shift();
    let [docs_rank, docs_idx] = docs;

    if (list.some((elem) => docs_rank < elem[0])) {
      list.push(docs)
    } else {
      result.push(docs)
    }
  }
  return result;
}

let testCase = parseInt(input[0]);
let cur = 1;
while (cur < testCase * 2) {
  let [N, M] = input[cur].split(' ').map(Number);
  let rank = input[cur + 1].split(' ').map(Number);
  rank = rank.map((elem, idx) => [elem, idx])
  let result = printer(rank);
  console.log(result)
  console.log(result.findIndex((elem) => elem[1] == M) + 1)
  cur += 2
}


