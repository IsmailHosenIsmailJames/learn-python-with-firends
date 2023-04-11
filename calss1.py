def myFunction(num1:float, oparation:str, num2:float):
    if(oparation == '/'):
        result = num1 / num2
    elif(oparation == '*'):
        result = num1 * num2
    elif(oparation == '+'):
        result = num1 + num2
    elif(oparation == '-'):
        result = num1 - num2
    elif(oparation == '**'):
        result == num1 ** num2
    elif(oparation == '%'):
        result = num1 % num2
    elif(oparation == 'root'):
        result = num1 ** (1 / num2)
        
    return result

while True:
    x = myFunction(float(input()), input(), float(input()))
    print(x)