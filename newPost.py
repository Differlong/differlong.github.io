import os
import time

name = input("输入文件名: ")
name = name.replace(" ", "")
if ".md" not in name:
    name = name + ".md"

order = "hugo new post/" + name
print(order)
os.system(order)
print("success!!!")
time.sleep(10)
