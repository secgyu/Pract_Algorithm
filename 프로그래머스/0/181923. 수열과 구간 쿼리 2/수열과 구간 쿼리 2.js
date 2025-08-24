function solution(arr, queries) {
  const result = [];

  for (const [s, e, k] of queries) {
    let best = Infinity;

    for (let i = s; i <= e; i++) {
      const v = arr[i];
      if (v > k && v < best) best = v;
    }

    result.push(best === Infinity ? -1 : best);
  }

  return result;
}