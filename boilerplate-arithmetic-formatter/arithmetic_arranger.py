
def errorCheck(problem=None, number1=None, operation=None, number2=None):
    if problem is not None:
        if len(problem) > 5:
            return True, 'Error: Too many problems.'

    if operation is not None:
        if operation not in '+-':
            return True, 'Error: Operator must be \'+\' or \'-\'.'

    if not (number1 is None and number2 is None):
        if not (number1.isnumeric() and number2.isnumeric()):
            return True, 'Error: Numbers must only contain digits.'
        if not (len(number1) <= 4 and len(number2) <= 4):
            return True, 'Error: Numbers cannot be more than four digits.'

    return False, 'No Errors'


def calculator(number1, operation, number2):
    result = 0
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2

    return str(result)


def arithmetic_arranger(problems, *args):

    ErrorValue = errorCheck(problems)
    if ErrorValue[0]:
        return ErrorValue[1]

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for index, items in enumerate(problems):
        item = items.split()

        num1 = item[0]
        num2 = item[2]
        oper = item[1]

        ErrorValue = errorCheck(number1=num1, operation=oper, number2=num2)
        if ErrorValue[0]:
            return ErrorValue[1]

        maxLength = len(num1) if len(num1) > len(num2) else len(num2)
    
        if (index > 0 and index < len(problems)):
            line1 += ''.rjust(4)
            line2 += ''.rjust(4)
            line3 += ''.rjust(4)

            if len(args) != 0:
                line4 += ''.rjust(4)

        line1 += num1.rjust(maxLength + 2) 
        line2 += oper + num2.rjust(maxLength + 1)
        line3 += ''.rjust(maxLength + 2, '-')

        if len(args) != 0:
            line4 += calculator(int(num1), oper, int(num2)) \
                                                .rjust(maxLength + 2)
    
    return f"{line1}\n{line2}\n{line3}" if len(line4) == 0 else f"{line1}\n{line2}\n{line3}\n{line4}"
    