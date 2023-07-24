print('h-----ello')
s3 = """Here is 
what you n
eed
do awesome thing"""
s1 = ('Hey'
      'How'
      'Do'
      'Away')
print(s1);

print(s3);

s4 = "oneTwo"

print('this \t is \n not good');

print(s4[1:4])

prime = [1, 3, 5, 7]
odd = [1, 3, 5]
odd.append(100)
print(prime + odd + [90] )

a  = [1, 2, 3, 4]
a[0:2] = []
print(a)
name,age = 'happy', 34
print(name,age)

i,j = 0, 1
#0, 1, 1, 2, 3, 5, 8, 13
fib = []
while i < 20:
      fib.append(i)
      i,j = j, i+j

print(fib)

i,j = 0, 1
while i < 20:
      print(i, end='#')
      i, j = j, i + j

#name = input('What is your name: ')
##print(name)
#age = input('What is your age: ')
#print ('Your name is ' + name + ' and your age is ' + str(age))

name = 'abc'
print(name, end="0")

for i in name:
      print(i)


d = {'ID': 200, 'Age': 23}
print(d.keys())
print(d.values())
for key, value in d.copy().items():
    if key == 200:
        prit('===>', 'range', key, str(value));
print('============>><<============')


for key, value in d.items():
      print(key, value, end="\n")
      
for i in range(10):
      print(i, end='#')
      
l1 = enumerate(['1', '2'])
print('\n')
l2 = list(l1);
x = 1
x2 = 10
print(eval('x+x2'))

print(sum(range(1000)))
print(len(range(1000)))




