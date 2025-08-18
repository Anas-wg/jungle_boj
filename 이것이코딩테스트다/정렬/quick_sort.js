let array = [4, 5, 6, 3, 1, 3, 4];

const quickSort = (arr, start, end) => {
  if (start >= end) {
    return;
  }

  let pivot = arr[end];
  let pIndex = start;

  for (let i = start; i < end; i++) {
    if (arr[i] < pivot) {
      [arr[i], arr[pIndex]] = [arr[pIndex], arr[i]];
      pIndex++;
    }
  }
  [arr[end], arr[pIndex]] = [arr[pIndex], arr[end]];

  quickSort(arr, start, pIndex - 1);
  quickSort(arr, pIndex + 1, end);
};

quickSort(array, 0, array.length - 1);
console.log(array);