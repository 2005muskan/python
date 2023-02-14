def sort ():
    A = int(input("Enter a value first:"))
    B = int(input("Enter a value second :"))
    operator = (input("Enter a operator(+,-,*,%,/,=) :"))

    if operator == "+":
        print(A+B)

    elif operator == "-":
        print(A-B)
     
    elif operator == "*":
        print(A*B)

    elif operator == "%":
        print(A%B)

    elif operator == "/":
        print(A/B)

    elif operator == "=":
        print(A=B)

    else:
        print(A**B)

print("your function")
sort()




        