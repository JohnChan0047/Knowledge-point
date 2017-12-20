# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/20 14:49'


def decorator_1(func):
    def wrapper():
        print('%s function is running.' % func.__name__)
        return func()
    return wrapper


@decorator_1
def test_1():
    print('Hello, World')


test_1()


def decorator_2(func):
    def wrapper(*args, **kwargs):
        print('%s function is running.' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@decorator_2
def test_2(str):
    print(str)


test_2('123456')