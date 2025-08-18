let array = [17, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 21];

// 1. Math.max()에 스프레드 연산자(...)를 사용해 배열의 최대값을 찾고
//    배열을 .fill(0)으로 초기화합니다.
let maxValue = Math.max(...array);
let count = new Array(maxValue + 1).fill(0);

// 2. 각 숫자의 등장 횟수를 셉니다.
for (let i = 0; i < array.length; i++) {
  count[array[i]] += 1;
}

// 3. 정렬된 결과를 담을 새로운 배열을 만듭니다.
let sortedArray = [];

// 4. count 배열을 순회하며 정렬된 결과를 sortedArray에 추가합니다.
for (let i = 0; i < count.length; i++) {
  for (let j = 0; j < count[i]; j++) {
    sortedArray.push(i);
  }
}

console.log(sortedArray);