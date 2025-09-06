function solution(arr, k) {
    var answer = [];
    if(k % 2 != 0){
        return arr.map(v => v * k)
    } else {
        return arr.map(v => v + k)
    }
}