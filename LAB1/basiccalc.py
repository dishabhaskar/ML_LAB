a = int(input("enter first number"))
b = int(input("enter second number"))
x = input("enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division\n")
if x == '1':
    res = a + b
    print("Addition", res)
elif x == '2':
    res = a - b
    print("Subtraction", res)
elif x == '3':
    res = a * b
    print("Multiplication", res)
elif x == '4':
    res = a / b
    print("Division", res)
else: 
     print("invalid inputs")
    
