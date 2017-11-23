# *args，**kwargs
Python允许程序员执行一个没有显式定义参数的函数，响应的方法是通过一个元祖（非关键字参数）或字典（关键字参数）作为参数组传递给函数。其中*args是以元祖形式体现的非关键字参数组，**kwargs是装有关键字参数的字典。

如果我们不确定往一个函数中传入多少参数，或者我们希望以元组（tuple）或者列表（list）的形式传参数的时候，我们可以使用*args（单星号）。如果我们不知道往函数中传递多少个关键词参数或者想传入字典的值作为关键词参数的时候我们可以使用**kwargs（双星号），args、kwargs两个标识符是约定俗成的用法。

```
def func(*args, **kwargs):
    print(args, kwargs)


li = [1, 2, 3]
tup = (2, 3, 4)
dic = {'s': 3, 'm': 4, 'c': 5}
a = 1
b = 2

func()
func(*li)
func(*tup)
func(*dic)
func(**dic)
func(li, dic, *li, **dic)
func(a, b, m=4, n=5)
```