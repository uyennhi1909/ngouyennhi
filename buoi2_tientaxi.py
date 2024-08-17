# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:37:38 2024

@author: UNHI
"""

# Bài tập tính tiền taxi
distance = float(input("Nhập số km quãng đường đi được: "))

if distance >= 0:
    # 1km đầu tiên
    if distance <= 1 : 
        tongtien = 20
        
    # 3km đầu tiên
    elif distance <= 3:
        tongtien = 20 + 13*(distance-1) 
        
    # Từ km thứ 4 đến km thứ 8
    elif distance <= 8 :
        tongtien = 20 + 13*(distance-1) + 12*(distance-3)
        
    # Giá còn lại
    else:
        tongtien = 20 + 13*(distance-1) + 12*(distance-3) + 10*(distance-8)
        
    # Áp dụng giảm giá  
    if tongtien >= 100 :
        tongtien = tongtien*(1 - 8/100)
        
    print(f"Tổng tiền taxi cần trả là {tongtien:.0f}k")
else:
    print("Không xác định")
    
        
       
        
    