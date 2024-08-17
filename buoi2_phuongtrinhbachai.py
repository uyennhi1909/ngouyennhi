# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:46:41 2024

@author: UNHI
"""

# Giải phương trình bậc hai
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
c = float(input("Nhập số thực c: "))
delta = float(b**2-4*a*c)

if delta == 0 :
    print("Vậy phương trình có nghiệm kép là: ", -b/(2*a) )
elif delta > 0:
    print("Vậy phương trình có 2 nghiệm phân biệt là: ", (-b + delta**0.5)/(2*a) ,"và ", (-b - delta**0.5)/(2*a) )
else:
    print("Vậy phương trình vô nghiệm") 
   
    