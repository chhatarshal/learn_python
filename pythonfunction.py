

l1 = 'This is LLL!'


def getDef(val):
    test = """This is three string"""
    val = test + l1
    #l1 ='value is here'
    print(f'This is a good work {val}')

getDef('value')

print(l1)

l4 = 4
def testL(arg = l4):
    print('value of l4: ' + str(l4))
def printL(x, L=[]):
    L.append(x)
    return L

l3 = 90
l4 = 100
testL()
print(printL(1))
print(printL(2))
print(printL(22, []))
print(printL(3))


def testF(arg1, *arg2, **arg3):
    print(arg1, arg2)
    print(arg3)

testF('1')
testF('1', 1)
testF('2', 1,2)
testF('1', 1, 2, age=24, name='Happy')