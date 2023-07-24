
print("Enter two numbers: \n")

a = ' '
while (not a.isnumeric()):
    a = input()
b = ''
while (not b.isnumeric()):
    b = int(input())
print("""Please enter :
1. For Addition
2. For subtraction
3. For Multiply
4. For divide""")

operation = int(input())

operations = {
    1 : lambda x,y : x + y,
    2 : lambda x,y : x - y,
    3 : lambda x,y : x*y,
    4 : lambda x,y : x/y
}

result = operations[operation](a,b)

print(result)