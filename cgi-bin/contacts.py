#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("Content-Type: text/html; charset=utf-8\n")

print("<html><body>")
print("<h1>Contact List (From File)</h1>")
print("<ul>")

# Lưu ý: ~/ không hoạt động trong script CGI, nên phải dùng đường dẫn tuyệt đối
# Thay [USER_CỦA_BẠN] bằng tên bạn thấy ở dòng lệnh (ví dụ: tracee)
file_path = "/home/tracee/contacts.txt"

try:
    with open(file_path, "r") as f:
        for line in f:
            if ":" in line:
                print(f"<li>{line.strip()}</li>")
except Exception as e:
    print(f"<li>Lỗi: {e}</li>")

print("</ul></body></html>")
