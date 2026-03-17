#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

print("Content-Type: text/html; charset=utf-8\n")
print("<html><body>")
print("<h1>Contact List (Từ Database MySQL)</h1><ul>")

try:
    # Kết nối vào MySQL (mặc định user root trên GCP không có pass)
    conn = mysql.connector.connect(
        host="localhost",
        user="tracee",      # Đổi từ root thành user vừa tạo
        password="123456",  # Nhập mật khẩu bà vừa đặt
        database="contact_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, email FROM contacts")
    
    for (name, phone, email) in cursor:
        print(f"<li>{name} : {phone} : {email or '-'}</li>")
        
    cursor.close()
    conn.close()
except Exception as e:
    print(f"<li>Lỗi kết nối DB: {e}</li>")

print("</ul></body></html>")
