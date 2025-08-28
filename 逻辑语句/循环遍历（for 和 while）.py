#### 循环（for / while） ####

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环语句只能用于任何可迭代的对象；break会中断循环；continue会跳出当前循环；pass保证代码的完整性；else会在没有中断循环的条件下执行。
for i in range(1, 3):
    print(i)
else:
    print('没有break中断退出')
print("------------------------------------------")
content = {'a': 90, 'b': [1, 2, 3], 'c': 'hello', 'd': []}.items()
for k, v in content:
    if k == 'd':
        break
    print(k, v, sep=' : ')
    pass
else:
    print('正常退出')
print("------------------------------------------")
n = 0
r = 0
while n <= 100:
    r += n
    n += 1
    continue
else:
    print(f'最后结果：{r}')
# 判断是否是闰年
def isRun() -> str:
    year = int(input("请输入一个年份: "))
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        print('{0} 是闰年' .format(year))
    else:
        print('{0} 不是闰年' .format(year))
#isRun()