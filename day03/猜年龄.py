#!/usr/bin/env python
#   -*- coding:utf-8 -*-
#   name:嘿嘎嘎
#   猜年龄游戏

count = 0
oldboy = 30
while True:
    print("这是第%d次" % count)
    count += 1
    age = int(input("猜我多大了："))
    if age == oldboy:
        print("你猜对了")
        break
    else:
        if age > oldboy:
            print("我还年轻")
            continue
        else:
            print("我很老了！")
            continue
print("你猜了%s次" % count)