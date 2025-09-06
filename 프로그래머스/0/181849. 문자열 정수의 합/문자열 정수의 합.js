function solution(num_str) {
    return [...num_str].reduce((sum, ch) => sum + Number(ch), 0)
}