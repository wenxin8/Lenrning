# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:28:34 2020

@author: zhong
"""
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property  # 访问器
    def name(self):
        return self.__name
    
    @name.setter  # 修改器
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    
def main():
    a = Student("张三", 25)
    print(a.name, a.age)
    a.name = "李四"
    a.age = 30
    print(a.name, a.age)
main()