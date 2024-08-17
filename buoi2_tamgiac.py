# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:11:33 2024

@author: UNHI
"""

# Bài tập tam giác

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a+b>c and a+c>b and b+c>a:
    #tam giác đều
    if a ==  b == c:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác đều")
    #tam giác cân
    elif a == b or a == c or b == c:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác cân")
    #tam giác vuông
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác vuông")
    else:
        print("a,b,c là 3 cạnh của tam giác")
else:
    print("a,b,c không là 3 cạnh của tam giác")
    
    