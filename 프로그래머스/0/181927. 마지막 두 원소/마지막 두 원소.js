function solution(num_list) {
    const last = num_list[num_list.length - 1]
    const prev = num_list[num_list.length - 2]
    
    if(last > prev) {
        num_list.push(last-prev)
    }else{
        num_list.push(last * 2)
    }
    return num_list
}