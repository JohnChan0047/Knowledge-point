# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/21 22:41'
import copy


a = [1, 2, 3, 4, ['a', 'b']] # 原始对象

b = a # 赋值
c = copy.copy(a) # 浅拷贝
d = copy.deepcopy(a) # 深拷贝

a.append(5) # 修改对象 a
a[4].append('c') # 修改对象a中的['a', 'b']数组对象

print('a: ', a) # a:  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('b: ', b) # b:  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('c: ', c) # c:  [1, 2, 3, 4, ['a', 'b', 'c']]
print('d: ', d) # d:  [1, 2, 3, 4, ['a', 'b']]