function solution(myString, pat) {
    const swap = [...myString].map(ch => (ch === 'A' ? 'B' : 'A')).join('')
    return swap.includes(pat) ? 1 : 0
}