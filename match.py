

def mt(tp):
    match tp:
        case (0, 0):
            print('origin')
        case (1, 2):
            print(f"value of x = " + str(1))
        case (a, b):
            print('value of sum ' +  str(a + b))
            
mt((1, 2))
mt((0, 0))
mt((10, 20))

data = [x for x in range(10)]
print(data)
for x in range(10):
    print('value 0f x ' + str(x))
else:
    print('else of for loop')




        