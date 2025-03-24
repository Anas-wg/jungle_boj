// JS에는 조합/순열 모듈이 없어요ㅠ

const getCombination = (arr, n) => {

  if (n === 1) return arr.map(el => [el]);
  // 최종 결과를 담을 배열
  const result = [];

  // fixed : 고정할 원소, origin : 원본 배열
  arr.forEach((fixed, idx, origin) => {
    // 현재 고정한 원소 이후의 배열을 나머지로 선언
    const rest = origin.slice(idx + 1);
    // 나머지와 n-1을 다시 전달하여 재귀호출
    const combis = getCombination(rest, n - 1);
    // 재귀호출이 끝나고 돌아오는 시점은
    // 처음 고정한 fixed로 구성 가능한 모든 조합을 리턴받은 이후
    // 따라서 리턴받은 값과 fixed를 다시 합쳐주어 조합 구성
    const attached = combis.map(combi => [fixed, ...combi]);
    // 구성된 조합 배열을 결과에 푸시
    result.push(...attached);
  });

  // 위에서 모든 재귀호출이 종료되면 저장된 조합 경우의 수 리턴
  return result;
}