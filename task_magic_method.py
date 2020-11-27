# task1
# class Mylist(list): 
#     def __getitem__(self, index):
#         return super().__getitem__(index - 1) 
# s = Mylist(range(1,10)) 
# print(s[1])

# task2
# class Student(dict): 
#     def __init__(self, name, lastname, group, mark) : 
#         self.name = name
#         self.lastname = lastname
#         self.group = group
#         self.mark = mark 

#     def __gt__(self, other):
#         total = sum([v for v in self.mark.values()])
#         average = total / len(self.mark)
#         total1 = sum([v for v in other.mark.values()])
#         average1 = total1 / len(other.mark)
#         return f'{self.name} средний балл {average} больше чем у {other.name} - {average1}'

#     def __lt__(self, other):
#         total = sum([v for v in self.mark.values()])
#         average = total / len(self.mark)
#         total1 = sum([v for v in other.mark.values()])
#         average1 = total1 / len(other.mark)
#         return f'{self.name} средний балл {average} меньше чем у {other.name} - {average1}'

# pasha = Student('Pasha', 'Strelcov', '10a', {'history' : 5, 'math' : 3, 'literature' : 4})
# sasha = Student('Sasha', 'Smirnov', '10b', {'history' : 2, 'math' : 4, 'literature' : 5}) 
# print(pasha > sasha) 
# print(sasha < pasha)

# task3
# import math

# class Complex(object): 
#     def __init__(self, real, i):
#         self.real = real
#         self.i = i
#     def __add__(self, num):
#         return Complex(self.real + num.real, self.i + num.i) 
#     def __sub__(self, num):
#         return Complex(self.real - num.real, self.i - num.i) 
#     def __mul__(self, num):
#         return Complex(self.real * num.real - self.i * num.i, self.real * num.i + self.i * num.real) 
#     def __truediv__(self, num):
#         aver = num.real ** 2 + num.i ** 2
#         return Complex((self.real * num.real + self.i* num.i) / aver, (self.i * num.real - self.real * num.i) / aver)
#     # def mod(self):
#     #     return Complex((self.real ** 2 + self.i ** 2) ** (1 / 2), 0) 

# first = complex(*map(float, input('введите число: ')))
# second = complex(*map(float, input('введите число: ')))
# print(first + second)
# print(first - second)
# print(first * second)
# print(first / second)
# # print(first.mod())
# # print(second.mod())

