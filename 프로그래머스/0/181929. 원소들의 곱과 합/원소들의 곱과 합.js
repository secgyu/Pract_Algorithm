function solution(num_list) {
    let total_sum = 0;
    let time_sum = 1;

    for (let i = 0; i < num_list.length; i++) {
        time_sum *= num_list[i];
        total_sum += num_list[i];
    }

    total_sum = total_sum * total_sum;

    if (time_sum < total_sum) return 1; 
    else return 0;
}