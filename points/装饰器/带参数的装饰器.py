# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/20 14:56'
import time


def decoretor_1(time):
    def wrapper_1(func):
        def wrapper_2():
            print('%s %s is running.' % (time, func.__name__))
            return func()
        return wrapper_2
    return wrapper_1


time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


@decoretor_1(time)
def test_1():
    print('Hello World')


test_1()


def decoretor_2(time):
    def wrapper_1(func):
        def wrapper_2(*args, **kwargs):
            print('%s %s is running.' % (time, func.__name__))
            return func(*args, **kwargs)
        return wrapper_2
    return wrapper_1


@decoretor_2(time)
def test_2(str):
    print(str)


test_2('123456')