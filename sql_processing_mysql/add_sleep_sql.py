# -*- coding:utf-8 -*-
# Author SHENGMINJIE.CN
# used by python3
# import sql insert 'select sleep(seconds)'

import datetime
filenametime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def add_sleep_sql(sourcefile, nums, second):

    #原始文件
    f = open(sourcefile, 'r+')
    #新文件
    t = open(filenametime+'.sql', 'w+')

    n = 1
    for i in f.readlines():
        t.write(i)
        if n % nums == 0:
            t.write("select sleep("+second+");\n")
            #f.write("select sleep(1);\n")
        n = n + 1
    f.close()
    t.close()

if __name__ == "__main__":
    sourcefile = input("请输入原始文件路径\n")
    nums = input("请输入间隔行数：（通常是5000）\n")
    nums = int(nums)
    second = input("请输入睡眠秒数：（通常是1）\n")
    second = str(second)
    add_sleep_sql(sourcefile, nums, second)
    print("done")