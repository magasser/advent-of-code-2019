def handle_opcode(op, src1, src2):
    res = 0
    if op == 1:
        res = src1 + src2
    elif op == 2:
        res = src1 * src2

    return res


def handle_prog(code):
    ip = 0
    while code[ip] != 99:
        length = len(code)
        if length > ip and length > code[ip + 1] and length > code[ip + 2] and length > code[ip + 3]:
            code[code[ip + 3]] = handle_opcode(code[ip], code[code[ip + 1]], code[code[ip + 2]])
        ip += 4

    return code


def calc_res_for(nr):
    for noun in range(0, 99):
        for verb in range(0, 99):
            code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
            code[1] = noun
            code[2] = verb
            handle_prog(code)
            out = code[0]
            if out == nr:
                return 100 * noun + verb

    return -1


print(calc_res_for(19690720))