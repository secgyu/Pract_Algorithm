const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    const value = Number(input[0]) + Number(input[1]);
    console.log(Number(input[0]) + ` + ` + Number(input[1]) + ` = ` + value)
});