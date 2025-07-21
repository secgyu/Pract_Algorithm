function solution(num_list) {
    let odd = '';
    let even = '';

    for (let num of num_list) {
        if (num % 2 === 0) {
            even += num;
        } else {
            odd += num;
        }
    }

    return parseInt(odd) + parseInt(even);
}