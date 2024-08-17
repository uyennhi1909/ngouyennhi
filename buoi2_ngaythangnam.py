# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:33:50 2024

@author: UNHI

"""

# Bài tập kiểm tra ngày tháng năm hợp lệ

time = input("Nhập ngày tháng năm theo đúng định dạng: ")

# Tách ngày tháng năm
try:
    ngay, thang, nam = map(int, time.split("/")) 
except ValueError:
    print("Định dạng ngày tháng năm không hợp lệ. Vui lòng nhập lại đúng định dạng")
else:
    # Kiểm tra năm nhuận
    if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
        namnhuan = True
    else:
        namnhuan = False

    # Những ngày trong tháng
    ngaytrongthang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Chỉnh sửa lại tháng 2 nếu là năm nhuận
    if namnhuan:
        ngaytrongthang[1] = 29 # sửa lại tháng 2 có 29 ngày

    # Kiểm tra ngày tháng năm hợp lệ
    if nam < 1:
        print("Năm không hợp lệ.")
    elif thang < 1 or thang > 12:
        print("Tháng không hợp lệ.")
    elif ngay < 1 or ngay > ngaytrongthang[thang - 1]:
        print("Ngày không hợp lệ.")
    else:
        print("Ngày, tháng, năm hợp lệ.")



