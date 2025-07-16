function solution(a, b) {
    const atob = String(a) + String(b)
    const btob = String(b) + String(a)
    return atob >= btob ? Number(atob) : Number(btob)
}