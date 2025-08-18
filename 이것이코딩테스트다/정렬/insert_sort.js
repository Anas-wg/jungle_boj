array = [4, 5, 6, 3, 1, 3, 4];

for (let i = 1; i < array.length; i++) {
  for (let j = i; j > 0; j--) {
    if (array[j] < array[j - 1]) {
      [array[j], array[j - 1]] = [array[j - 1], array[j]]
    } else {
      break
    }
  }
}

console.log(array)