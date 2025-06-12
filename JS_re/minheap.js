class minHeap {
  constructor() {
    this.heap = [null];
  }

  getSize() {
    return this.heap.length - 1;
  }

  isEmpty() {
    return this.heap.length < 2
  }

  insert(node) {
    let current = this.heap.length; // 현재 가장 마지막 노드
    while (current > 1) {
      // 현재 위치에서 루트까지 이동, MinHeap 요건 맞을때까지 비교 &* 교환
      const parent = Math.floor(current / 2); // current의 부모노드
      if (heap[parent] > node) {
        this.heap[current] = this.heap[parent] // minHeap이기때문에 부모 노드가 더 크면 서로 교환
        current = parent // 현위치에 부모였던 노드 박기
      } else {
        break; // MinHeap 만족하기에 break
      }
    }
    this.heap[current] = node; // 현재 노드에 node 값 부여
  }

  remove() {
    let min = this.heap[1]; // 0번은 null, Root node
    if (this.heap.getSize() === 1) {
      this.heap = [null];
      return min;
    }

    this.heap[1] = this.heap[this.getSize()] // 루트를 마지막으로 이동
    this.heap.pop() // 루트로 옮겼던 마지막 노드 삭제

    // 힙 재정렬

    let current = 1;
    while (true) {
      let leftChild = current * 2;
      let rightChild = (current * 2) + 1;
      let smallestChild = null; // 가장 작은 값 가진 자식의 인덱스

      // 왼쪽자식 확인
      if (leftChild <= this.getSize()) {
        smallestChild = leftChild;
        // 왼쪽자식, 오른쪽자식 둘다 있는 경우 + 오른쪽자식이 더 작은지 확인
        if (rightChild <= this.getSize() && this.heap[rightChild] < this.heap[leftChild]) {
          smallestChild = rightChild
        }
      } else {
        break; // 자식 없으면 시마이
      }
      // 현재 노드가 가장 작은 자식보다 작거나 같으면 힙 조건 만족, 반복 종료
      if (this.heap[current] <= this.heap[smallestChild]) {
        break;
      }
      // 현재 노드와 가장 작은 자식 노드 위치 교환
      [this.heap[current], this.heap[smallestChild]] = [this.heap[smallestChild], this.heap[current]]; 
    }
    return min; // 저장해둔 최솟값 반환
  }
}