# accepted by Kattis

m = int(input())
operations = ['+', '-', '*', '//']

possibleResult = {}

for op1 in operations:
    for op2 in operations:
        for op3 in operations:
            equationStr = '4 ' + op1 + ' 4 ' + op2 + ' 4 ' + op3 + ' 4'
            result = eval(equationStr)
            possibleResult[result] = equationStr.replace('//','/')

for i in range(m):
    n = int(input())
    if n in possibleResult:
        print(str(possibleResult[n]) + ' = ' + str(n))
    else:
        print('no solution')