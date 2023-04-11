ans = 0

def myFunction(ex: str):
    global ans
    spdt = ex.split(" ")
    if (spdt[0] == "ans" or spdt[0] == "Ans"):
        num1 = ans
    else:
        num1 = float(spdt[0])

    oparation = spdt[1]

    if (spdt[2] == "ans" or spdt[2] == "Ans"):
        num2 = ans
    else:
        num2 = float(spdt[2])

    if (oparation == '/'):
        result = num1 / num2
    elif (oparation == '*'):
        result = num1 * num2
    elif (oparation == '+'):
        result = num1 + num2
    elif (oparation == '-'):
        result = num1 - num2
    elif (oparation == '**'):
        result == num1 ** num2
    elif (oparation == '%'):
        result = num1 % num2
    elif (oparation == 'root'):
        result = num1 ** (1 / num2)

    ans = result
    return result


while True:
    x = myFunction(input())
    print("=", x)
