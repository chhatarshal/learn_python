

def info(name, /, *birth, **allInfo):
    print(name, ' here is age ' + str(birth))
    print("All Information of this person: " + str(allInfo))


info('FirstName', 24, 2000, name="FirstName", age=24, dateofbirth=2000)

def testName(name,/, **arg):
    print(name)
    print(arg)

testName('n1', name='abc')


def docFun():
    """Here is some awesome document."""

print(docFun.__doc__)


def annotation(para1, para2='90') -> str:
    print(annotation.__annotations__);
    return para2 + para1;

print(annotation('one1'))


def testUnpack(name, age, /):
    print('Hey here is my name: ' + name)
    print('Hey here is my age: ' + str(age))

testUnpack('happy', 23)

testUnpack(*('happy', 23))