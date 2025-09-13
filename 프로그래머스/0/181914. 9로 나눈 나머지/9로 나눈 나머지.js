function solution(number) {
    let sum = 0
    for (const ch of number) {
        sum += parseInt(ch)
    }
    return sum % 9
}