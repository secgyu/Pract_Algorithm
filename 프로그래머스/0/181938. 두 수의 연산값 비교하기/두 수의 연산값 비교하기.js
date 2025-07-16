function solution(a, b) {
    const result1 = String(a) + String(b)
    const result2 = 2 * a * b
    
    return result1 > result2 ? Number(result1) : result2 
}