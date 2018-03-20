#############内置函数##################
#
#
#############abs()####################
#函数返回数字的绝对值
#语法abs(x)
# print(abs(50))
# print(abs(-50))
############dict()####################
#函数用于创建一个字典
#class ditc(**kwarg)
#class ditc(mapping,**kwarg)
#class ditc(iterable,**kwarg)
# print(dict(a="a",b="b",c="c"))
# 映射函数方式构造字典
# print(dict (zip(['a','b','c'],[1,2,3])))
# print(dict([("a",1),("b",2),("c",3)]))
# ##########help()####################
# 返回对象帮助信息
# help([object])
# a=(1,2,3)
# print(help(a))
# import sys
# print(help(sys))
# ###############min()################
# 方法查看参数的最小值，参数可以为序列
# 语法min( x, y, z, .... )
# print(min(1,2,5,9))
# 
# 
# ###############setattr()############
# setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在。
# 语法 setattr(object, name, value)
# import setattr
# class A:
# 	num=5
# a=A()
# setattr(a,'num',9)#设置属性的值
# print(a.num)
# ################all()###############
# 函数用于判断参数的值是否为0
# all(元祖或者列表)
# print(all(['a', 'b', 'c', 'd']))
# print(all(['a', '', 'c', 'd']))
# print(all(()))
# print(all({}))
# ##############dir()################
# 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表
#语法dir()
# print(dir())
# ############ hex()#################
#hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
#hex(x)
# print(hex(20))
# #############next() ##############
# next() 返回迭代器的下一个项目
#next( 可迭代对象[, default])
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break
##############slice()################
#slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
#class slice(起始, 结束[, 间距])
#
# myslice = slice(5)# 设置截取5个元素的切片
# arr = range(10)
# print(arr[myslice])
# 
##############any()################
# any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象
# 如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。
# any(元祖或者列表)
# print(any(['a', 'b', 'c', 'd']))
# print(any(""))
##############divmod()################
#函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
#divmod(a, b)
# print(divmod(7, 2))
# print(divmod(8, 2))
##############id() ################
#函数用于获取对象的内存地址。
#id([object])
# print(id('a'))
# print(id(5))
##############sorted()################
# 函数对所有可迭代的对象进行排序操作。
#sorted( 可迭代对象, key=None, reverse=False)
# print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))
# example_list = [5, 0, 6, 1, 2, 7, 3, 4]
# print(sorted(example_list, reverse=True))
##############ascii()################
# ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 
# ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。 生成字符串类似 Python2 版本中 repr() 函数的返回值。
# ascii(object)
# print( ascii('runoob'))
############## enumerate()################
#enumerate() 函数用于将一个可遍历的数据对象
#(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# enumerate(迭代器或者序列, 下标起始位置)
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
##############  input()################
#raw_input() 将所有输入作为字符串看待，返回字符串类型。
#而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）
##############oct()################
#oct() 函数将一个整数转换成8进制字符串。
#oct(x)
# print(oct(52))
# ###########staticmethod() ##############
# python staticmethod 返回函数的静态方法。
# 静态方法无需实例化
# ###########bin() ##############
# bin() 返回一个整数 int 或者长整数 long int 的二进制表示
# bin(x)
# print(bin(5))
# ###########eval() ##############
# eval() 函数用来执行一个字符串表达式，并返回表达式的值
# eval(expression[, globals[, locals]])
# 
# x=7
# print(eval('3*x'))
# ########### int() ##############
# int() 函数用于将一个字符串或数字转换为整型。
###############open()#################
#打开一个文件夹
###############str()#################
#str() 函数将对象转化为适于人阅读的形式
###############bool()#################
# 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
# print(bool(0))
# print(bool(5))
############### exec #################
# exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。
# exec(object[, globals[, locals]])
# x = 10
# expr = ""
# z = 30
# # sum = x + y + z
# print(sum)
# def func():
#     y = 20
#     exec(expr)
#     exec(expr, {'x': 1, 'y': 2})
#     exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    
# func()
###############  isinstance()  #################
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
# isinstance(object, classinfo)
# class A:
#     pass
 
# class B(A):
#     pass
 
# print(isinstance(A(), A))   # returns True
# print(type(A()) == A)        # returns True
# print(isinstance(B(), A))  # returns True
# print(type(B()) == A)
############### pow()#################
# pow() 方法返回 xy（x的y次方） 的值。
# import math

# # math.pow( x, y )
# print ("math.pow(100, 2) : ", math.pow(100, 2))
# print ("math.pow(100, -2) : ", math.pow(100, -2))
############### ord()#################
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）
# 的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，
# 或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
# ord(c)
############### sum()#################
#sum() 方法对系列进行求和计算
#sum(iterable[, start])
# print(sum((2, 3, 4), 1) )
############### bytearray()#################
# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
############### filter()#################
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表
# filter(function, iterable)
###############  issubclass()#################
# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
# issubclass(class, classinfo)
# 
# class A:
#     pass
# class B(A):
#     pass
####################super()###################
#子类调用父类的一种方法
#super()子类()
# class A:
#     pass
# class B(A):
#     def add(self, x):
#         super().add(x)
#####################bytes###################
#函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。
#语法class bytes([source[, encoding[, errors]]])
#####################float()###################
#float() 函数用于将整数和字符串转换成浮点数
#class float([x])
##################### iter()###################
#iter() 函数用来生成迭代器
#iter(object[, sentinel])
##################### print()###################
#
#print() 方法用于打印输出，最常见的一个函数。
#
##################### tuple###################
#tuple 函数将列表转换为元组。
#tuple( seq )
# list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# print(tuple(list1))
#####################callable()###################
#函数检查一个对象是否被可以调用
#callable(object)
#####################format###################
#制定字符串的排列顺序
#{}{}.format(排序内容)
#####################len()###################
#len() 方法返回对象（字符、列表、元组等）长度或项目个数。
##################### property()###################
#property() 函数的作用是在新式类中返回属性值。
#################### type()###############
#type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
####################  chr()###############
#chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
# print(chr(0x30), chr(0x31), chr(0x61))
# ###################### frozenset()############
# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
# ######################  list()############
# 将元粗转换为列表
# list(转换的元祖)
# ###################### vars()############
# vars() 函数返回对象object的属性和属性值的字典对象。
# 333############classmethod()##############
# 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
# class A(object):
#     bar = 1
#     def func1(self):  
#         print ('foo') 
#     @classmethod
#     def func2(cls):
#         print ('func2')
#         print (cls.bar)
#         cls().func1()   # 调用 foo 方法
 
# A.func2()  
# ############getattr()##############
# getattr() 函数用于返回一个对象属性值。
# getattr(object, name[, default])
# ############locals() ##############
#  函数会以字典类型返回当前位置的全部局部变量。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True
# def runoob(arg):    # 两个局部变量：arg、z
# 	z = 1
# 	print (locals())
# runoob(4)
# ############ repr()  ##############
# repr() 函数将对象转化为供解释器读取的形式。

# >>>s = 'RUNOOB'
# >>> repr(s)
# "'RUNOOB'"
# >>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
# >>> repr(dict)
# "{'google': 'google.com', 'runoob': 'runoob.com'}"
# >>>
# ############  zip()  ##############
# 数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# 
# ###################### compile()############################
# compile() 函数将一个字符串编译为字节代码。
# ###################### map() ############################
# 会根据提供的函数对指定序列做映射。

# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# ######################reversed###########################
# reversed 函数返回一个反转的迭代器
#  
# 字符串
# seqString = 'Runoob'
# print(list(reversed(seqString)))
 
# # 元组
# seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
# print(list(reversed(seqTuple)))
 
# # range
# seqRange = range(5, 9)
# print(list(reversed(seqRange)))
 
# # 列表
# seqList = [1, 2, 4, 3, 5]
# print(list(reversed(seqList)))
#####################################complex() ########################
#complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
#####################################hasattr() ########################
#hasattr() 函数用于判断对象是否包含对应的属性。
#hasattr(object, name)
# class Coordinate:
#     x = 10
#     y = -5
#     z = 0
 
# point1 = Coordinate() 
# print(hasattr(point1, 'x'))
# print(hasattr(point1, 'y'))
# print(hasattr(point1, 'z'))
# print(hasattr(point1, 'no'))
##################################### max()########################
# max() 方法返回给定参数的最大值，参数可以为序列。
# print ("max(80, 100, 1000) : ", max(80, 100, 1000))
# print ("max(-20, 100, 400) : ", max(-20, 100, 400))
# print ("max(-80, -20, -10) : ", max(-80, -20, -10))
# print ("max(0, 100, -400) : ", max(0, 100, -400))
##################################### round()########################
#round() 方法返回浮点数x的四舍五入值。

# print ("round(70.23456) : ", round(70.23456,1))
# print ("round(56.659,1) : ", round(56.659,1))
# print ("round(80.264, 2) : ", round(80.264, 2))
# print ("round(100.000056, 3) : ", round(100.000056, 3))
# print ("round(-100.000056, 3) : ", round(-100.230056, 3))
#####################################delattr()########################
#delattr 函数用于删除属性。
#delattr(object, name)
# class Coordinate:
#     x = 10
#     y = -5
#     z = 0
 
# point1 = Coordinate() 
 
# print('x = ',point1.x)
# print('y = ',point1.y)
# print('z = ',point1.z)
 
# delattr(Coordinate, 'z')
 
# print('--删除 z 属性后--')
# print('x = ',point1.x)
# print('y = ',point1.y)
 
# # 触发错误
# print('z = ',point1.z)
##################################### hash()########################
#hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
# hash(object)
# 
# print(hash('test'))
#####################################memoryview()########################
# 函数返回给定参数的内存查看对象(Momory view)。

# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。
# memoryview(obj)
# #############################set()#########################
# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。