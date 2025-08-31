function solution(n) {
    var answer = [];
    answer.push(n)
    while(1){
        if(n === 1) break
        if(n % 2 === 0){
            n /= 2
            answer.push(n)
        }else{
            n = 3*n+1
            answer.push(n)
        }
    }
    return answer;
}