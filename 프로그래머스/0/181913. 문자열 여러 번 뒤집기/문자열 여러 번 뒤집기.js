function solution(my_string, queries) {
    let arr = my_string.split("");
  for (const [s, e] of queries) {
    const sub = arr.slice(s, e + 1).reverse();
    arr.splice(s, e - s + 1, ...sub);
  }
  return arr.join("");
}