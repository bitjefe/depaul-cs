// works but not accepted by all Kattis tests

var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const ops = ['+','-','*','/']

var lines = []; 

rl.on('line', function (line) {
    lines.push(line)
    
    let num = lines[0];
    
    if (lines[num]) {
        for (i=1; i<lines.length; i++) {
            fourThought(lines[i])
        }
        rl.close();
        process.exit(0);
    }
})

function fourThought(line) {
    for (const op1 in ops ) {
        for (const op2 in ops) {
            for (const op3 in ops) {
                let opString = '4 ' + ops[op1] + ' 4 ' + ops[op2] + ' 4 ' + ops[op3] + ' 4'
                
                if (eval(opString) == parseInt(line)){
                    console.log(opString, ' = ', line)
                    return
                }
            }
        }
    }
    console.log("no solution")
    return
}