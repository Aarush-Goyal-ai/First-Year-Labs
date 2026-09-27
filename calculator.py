def calculator():
    a = float(input("Enter First Number:"))
    op = input("Enter Operator you want to use (+,-,*,/,%,//):")
    b = float(input("Enter Second Number:"))
    if op=='+':
        result= a+b
    elif op=='-':
        result= a-b
    elif op== '*':
        result= a*b
    elif op== '/':
        if b==0:
         result=("Error Division by Zero")
        else:
            result= a/b
    elif op== '%':
        if b==0:
            result=("Error Division by Zero")
        else:
            result= a%b
    elif op== '//':
        if b==0:
            result=("Error Division by Zero")
        else:
            result= a//b
    
    else:
        print("INVALID CHOICE!")
        
    print("Result:",result)
    
calculator()
