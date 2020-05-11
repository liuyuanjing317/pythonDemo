# 2020 0506 练习demo
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('Do you really want to quit?')


def f(a, L=[]):
    L.append(a)
    return L


# print(f(1))
# print(f(2))
# print(f(3))

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
#print(stack)
#print(stack.count(2))
#print(stack.pop())
#print(stack)


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
#print(queue.popleft() )                # The first to arrive now leaves
#print(queue.popleft()  )                # The second to arrive now leaves
#print(queue )                           # Remaining queue in order of arrival
queue=deque(['Michael', 'Terry', 'Graham'])
#print(queue )


squares = []
for x in range(10):
    squares.append(x**2)
#print(squares )


squares = list(map(lambda x: x**2, range(10)))
#print(squares )
squares = [x**2 for x in range(10)]
#print(squares )

list1=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#print(list )

from math import pi
pilist=[str(round(pi, i)) for i in range(1, 6)]
#print(pilist)


matrix = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12]
   ]
mx=[[row[i] for row in matrix] for i in range(4)]
#print(mx)

#mx1=matrix(zip(*matrix))
#print(mx1)
del mx[:]
#print(mx)

#元组
t = 12345, 54321, 'hello!'
#print(t)
#print(t[0])

u = t, (1, 2, 3, 4, 5)
#print(u)

#元组不允许单独为其中的元素赋值
#t[0] = 88888
#print(t[0])


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

t='orange' in basket
print(t)
a = set('abracadabra')
print(a)
b = set('alacazam')
#print(b)
#a 与b 的差集
#print(a-b)
# b与a 的差集
#print(b-a)
#并集
#print(a | b)
#交集
#print(a &  b)
#a不在b中的数据
#print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
#print(a)


tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
tel['sape'] = 4138
print(tel)

del tel['sape']
print(tel)

#=list(tel)
print(list(tel))
print(sorted(tel))

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x**2 for x in (2, 4, 6)})

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
questions = ['name', 'quest', 'favorite color','test']
answers = ['lancelot', 'the holy grail', 'blue','yes']
# zip：合并两个数组；当两个数组长度不一致时，多余的数据会被抛弃
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#reversed 倒序 ；range（起点，终点，步长）
for i in reversed(range(1, 10, 2)):
    print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#sorted 排序
for f in sorted(set(basket)):
    print(f)


import math
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    #不是nan判断
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

#运算符比较 短路运算符
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
print(string1 or string2 or string3)



#模块
import   method as mt
mt.fib(1000)
#print(mt.fib2(1000))


import sys
#print(sys.path)


#输入输出
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
s='{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(s)


import math
#数字后加f 是对数据长度的格式化
print(f'The value of pi is approximately {math.pi:.3f}.')



table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
#  ：10d 格式化输出数据指定宽度
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    'Dcab: {0[Dcab]:d}'.format(table))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x**3))

#读取文件  'r+' 代表读写
f=open('C:/Users/Administrator/Desktop/text.txt', 'r+')
print(f.read())
f.write('This is a test\n')
f.closed

f=open('C:/Users/Administrator/Desktop/xxx.txt', 'r+')
import json
#格式化json
xc=json.dumps([1, 'simple', 'list'])
print(xc)
#json.dump(x, f)
#x = json.load(f)
#print(x)



class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def f(self):
        return 'hello world'


x = Complex(3.0, -4.5)
#print(x.r, x.i)
#print(x.f())



# 允许将外部方法赋予类的属性
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

xy= C
print(xy.f(xy,2,3))
print(xy.h(xy))


#允许使用self 关键字来调用类内部的其他方法 ，内部定义的初始化，代码需要进行初始化
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(self,x)
        self.add(self,x)

x1=Bag
x1.__init__(x1)
x1.add(x1,23232)
x1.addtwice(x1,1212121)
#print(x1.data)



#继承
class DerivedClassName(Bag):
    x1="nice day"
    x2="how"

    def speak(self):
        print(self.x1+self.x2)


x3=DerivedClassName
x3.__init__(x3)
x3.add(x3,232323)
#print(x3.data)
#print(x3.speak(x3))


class SecondFather():
    def second(self):
        print("i love china")
# 多重继承 只支持继承多个无关的类，若类之间有继承关系，则多重继承回报错 Cannot create a consistent method resolution
class MuiltImpl(SecondFather,DerivedClassName):
    pX=1
    py=2

    def userFather(self):
        self.__init__(self);
        self.add(self,self.px)

    def useSecondF(self):
        self.__init__(self);
        self.speak(self)



x5=MuiltImpl
x5.useSecondF(x5)
x5.second(x5)



class Mapping:
    def __init__(self, x):
        self.items_list = []
        self.__update(x)

    def update(self, x):
        for item in x:
            self.items_list.append(item)

    __update = update   # private copy of original update() method
#使用方法重命名的方式来重写父类的方法
class MappingSubclass(Mapping):
    items_list = []

    def update(self, keys, values):

        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

    def faUpdate(self,x):
        self.__update(self,x)

x7=MappingSubclass
#s = 'abcdefg'
#x7.__init__(x7,"1235641")

x7.update(x7,[1,2,3],[4,5,6])
print(x7.items_list)



# 空对象允许外部添加属性
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.name,john.dept,john.salary)


leo=Employee()
leo.wife='Lisa'
leo.child='Tony'
leo.sister='Tersa'

print(leo.child,leo.wife,leo.sister)
leo
# 获取对象属性的内置函数
print(dir(leo))
x10=dir(leo)
for item in x10:
    if item.__contains__('__'):
        pass
    else:
        print(item)


s="abc"
it=iter(s)
print(next(it))

#类里自定义迭代器，在进行for循环时回优先调用类里的迭代器
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)

#生成器表达式¶
print(sum(i*i for i in range(10))   )

#标准库 os 系统入口类
import os
print(os.getcwd() )
os.system('mkdir today')

# 文件管理或文件目录
import shutil
#shutil.copyfile('data.db', 'archive.db')

#文件通配符¶
import  glob
print(glob.glob('*.py'))

import sys
print(sys.argv)

# math 基础的数据操作
# python 虚拟环境用于解决不同模块之间版本依赖的问题  venv

# pyhton 在进行浮点运算时，底层 的运算机制是以二进制来计算的，计算结果与十进制的计算结果有误差，
# 比如 1/10 以十进制计算可得 0.1，但是以二进制计算只会无限趋近于0.1 ，
# 在计算时可以使用四舍五入获得想要的结果 python 提供了精确计算的库可使用 https://scipy.org/，
# 在需要十进制精确计算的情况下可使用decimal 模块，有理数的运算可使用 fractions模块来实现
#表示性错误 是指某些（其实是大多数）十进制小数无法以二进制（以 2 为基数的计数制）精确表示这一事实造成的错误。
# 这就是为什么 Python（或者 Perl、C、C++、Java、Fortran 以及许多其他语言）经常不会显示你所期待的精确十进制数值的主要原因


x = 3.14159
print(x.as_integer_ratio())
print(x == 3537115888337719 / 1125899906842624)

#print(2**52)
#print(2**53)
#print(2**56)

q, r = divmod(2**56, 10)
print(r)
print(q+1)

