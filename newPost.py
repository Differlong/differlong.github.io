import os
import time

name = input("输入文件名: ")
name = name.replace(" ", "")
order = "hugo new post/" + name + ".md"
print(order)
os.system(order)
print("success!!!")
time.sleep(10)
