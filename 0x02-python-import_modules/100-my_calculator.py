#!/usr/bin/python3
def calculator():
    import calculator_1 as cal
    import sys
    operators = {'+': cal.add, '-': cal.sub, '*': cal.mul, '/': cal.div}

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    for key, func in operators.items():
        if sys.argv[2] == key:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{:d} {} {:d} = {:d}".format(a, key, b, func(a, b)))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

if __name__ == "__main__":
    calculator()
