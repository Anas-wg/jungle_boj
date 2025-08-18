
array = [4, 5, 6, 3, 1, 3, 4];

for (let i = 0; i < array.length - 1; i++) {
  let minIdx = i // 고정 대상
  for (let j = i + 1; j < array.length; j++) {
    if (array[minIdx] > array[j]) {
      minIdx = j // 작은 것 찾기
    }
  }
  if (minIdx !== i) {
    // 가장 작은 값 찾은 후 한번만교환
    [array[i], array[minIdx]] = [array[minIdx], array[i]];
  }
}

console.log(array)