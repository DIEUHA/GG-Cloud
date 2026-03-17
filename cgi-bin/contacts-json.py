#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import json

# Khai báo với trình duyệt: "Tui gửi dữ liệu JSON đó nha"
print("Content-Type: application/json; charset=utf-8\n")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="tracee",
        password="123456",
        database="contact_db"
    )
    # dictionary=True giúp lấy dữ liệu ra dạng {key: value} giống JSON luôn
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, phone as telephone, email FROM contacts")
    
    rows = cursor.fetchall()
    
    # Tạo cấu trúc đúng y như đề bài yêu cầu
    result = {
        "ok": True,
        "count": len(rows),
        "data": rows
    }
    
    # Biến object Python thành chuỗi JSON và in ra
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    cursor.close()
    conn.close()

except Exception as e:
    print(json.dumps({"ok": False, "error": str(e)}))

