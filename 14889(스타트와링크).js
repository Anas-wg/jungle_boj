const fs = require("fs");
const input = fs.readFileSync('input.txt').toString().split('\n');


let N = parseInt(input[0]);
let ability = [];
let players = [];

for (let i = 1; i <= N; i++) {
  let arr = input[i].split(' ').map(Number);
  ability.push(arr);
}

for (let i = 1; i <= N; i++) {
  players.push(i)
}


const getCombinations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((el) => [fixed, ...el]);
    results.push(...attached);
  });
  return results;
}

const calculate_ability = (arr) => {
  let team_ability = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      let first = arr[i] - 1
      let second = arr[j] - 1
      team_ability += (ability[first][second] + ability[second][first])
    }
  }
  return team_ability
}

let answer = []

let combinations = (getCombinations(players, N / 2)).forEach((elem) => {
  let start = elem
  let link = players.filter((elem) => !start.includes(elem))
  let result = Math.abs(calculate_ability(start) - calculate_ability(link))
  answer.push(result)
});

// console.log(answer)

console.log(Math.min(...answer))
