const getPermutaion = (arr, n) => {
  if (n === 1) return arr.map(el => [el]);
  const result = [];

  arr.forEach((fixed, idx, origin) => {
    // 고정한 원소 fixed를 제외한 나머지 모든 배열이 나머지가 되어야 한다
    // 따라서 기존에 선택이 되었다고 할 지라도
    // 해당 원소를 다시 포함시켜 줌으로써 순서가 달라지는 경우까지
    // 모두 고려하여 경우의 수를 구성할 수 있다.
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
    const perms = getPermutation(rest, n - 1);
    const attached = perms.map(perm => [fixed, ...perm]);
    result.push(...attached);
  });

  return result;
}