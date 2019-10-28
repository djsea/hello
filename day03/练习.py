#!/usr/bin/env python
#   -*- coding:utf-8 -*-
#   name:嘿嘎嘎

"""
用户三次登录
1、功能拆分
2、拼凑功能
"""
"""
user = input("请输入用户名：")
pwd = input("请输入密码")


if user == "oldboy" and pwd == "123":
    print("登录成功")
else:
    print("登录失败")
"""
"""
count = 1
while count <=3:

    print(count)
    count += 1
"""

count = 1
while count <= 3:
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    if user == "boy" and pwd == "123":
        print("登录成功")
        break
    else:
        print("登录失败")
        if count == 3:
            print("超过三次")
            break
    count += 1