function solution(l, r) {
  const res = [];
  const q = [5];

  while (q.length) {
    const x = q.shift();
    if (x > r) continue;

    if (x >= l) res.push(x);

    const x0 = x * 10;    
    const x5 = x * 10 + 5; 
    if (x0 <= r) q.push(x0);
    if (x5 <= r) q.push(x5);
  }

  return res.length ? res : [-1];
}