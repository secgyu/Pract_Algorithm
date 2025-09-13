function solution(a, b, c, d) {
  const nums = [a, b, c, d];
  const cnt = new Map();
  for (const x of nums) cnt.set(x, (cnt.get(x) || 0) + 1);
  const kinds = cnt.size;
  if (kinds === 1) {
    const [[p]] = [...cnt.entries()];
    return 1111 * p;
  }
  for (const [x, c] of cnt) {
    if (c === 3) {
      const p = x;
      const q = [...cnt.keys()].find(k => k !== p);
      return (10 * p + q) ** 2;
    }
  }

  if (kinds === 2) {
    const [[p], [q]] = [...cnt.entries()];
    return (p + q) * Math.abs(p - q);
  }

  for (const [x, c] of cnt) {
    if (c === 2) {
      const singles = [...cnt.keys()].filter(k => k !== x);
      const [q, r] = singles;
      return q * r;
    }
  }

  return Math.min(...nums);
}
