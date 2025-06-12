const graph = {
  1: [2, 3],
  2: [4],
  3: [4, 5],
  4: [],
  5: []
};

function BFS(graph, start, visited) {
  const queue = [];
  queue.push(start);
  visited[start] = true;

  while (queue.length != 0) {
    const v = queue.shift();
    console.log(v);

    for (const node of graph[v]) {
      if (!visited[node]) {
        queue.push(node);
        visited[node] = true;
      }
    }
  }
}
let visited = new Array(5).fill(false)

BFS(graph, graph[0], visited)

