function solution(intStrs, k, s, l) {
    var answer = [];
    for(let i = 0; i < intStrs.length; i++){
        const part = intStrs[i].slice(s, s+l)
        const num = Number(part)
        if(num > k) answer.push(num)
    }
    return answer;
}