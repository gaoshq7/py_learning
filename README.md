# Python 学习项目 (py_learning)

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Platform-Cross--platform-orange" alt="Platform">
</div>

<br>

> 一个系统性的 Python 学习项目，涵盖从基础语法到高级特性的完整知识体系。通过丰富的代码示例和详细注释，帮助你深入理解 Python 编程语言的各个方面。

## 🌟 项目亮点

- 📚 **全面覆盖** - 从基础语法到高级特性，一站式学习
- 🧪 **实战代码** - 每个概念都配有可运行的示例代码
- 🎯 **结构清晰** - 按主题分类，便于查找和学习
- 💡 **详细注释** - 代码中包含丰富的解释说明
- 🚀 **即学即用** - 克隆即可运行，无需额外配置

## 📁 项目结构

```
py_learning/
├── 基础语法/
│   ├── 基本规范.py           # Python 编码规范
│   ├── 声明变量.py           # 变量声明方式
│   ├── 基本内置函数.py        # 常用内置函数
│   └── 包管理.py            # 模块与包管理
├── 数据类型/
│   ├── 基本数据类型/         # 数字、字符串、布尔值
│   └── 容器使用/            # 列表、元组、字典、集合
├── 控制结构/
│   ├── 逻辑语句/            # 条件判断、循环
│   └── 迭代器与生成器/       # 迭代器、生成器、列表推导式
├── 函数编程/
│   ├── 函数/                # 参数、返回值、匿名函数
│   └── 高级函数特性/         # 闭包、装饰器
├── 面向对象/
│   └── 类/                 # 类定义、继承、多态等
└── 并发编程/
    └── 进程与线程/          # 多线程、多进程编程
```


## 🎯 学习路径

### 1. 基础入门
```python
# 变量声明
a = b = c = 1
d, e, f = 4, [1,2,3,4], "liangdianshui"

# 基本数据类型操作
str1 = 'Hello World'
int1 = int('99')
list1 = [1, 2, 3, 4, 5]
```


### 2. 容器操作
```python
# 列表操作
l1 = ['哈哈', '呵呵', '哦哦', '嘻嘻']
l1.append('喔喔')
l1.reverse()

# 字典使用
d1 = dict(x='张三', y=90, h=['唱歌', '跳舞'])
for key, value in d1.items():
    print(f"{key}: {value}")
```


### 3. 函数编程
```python
# 匿名函数
square = lambda x: x ** 2
print(square(5))  # 25

# 高阶函数
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
squares = list(map(lambda x: x**2, nums))
```


### 4. 面向对象
```python
class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f'你好，{self.name}')

class VipUser(User):
    def greet(self):
        print(f'尊敬的VIP用户 {self.name}，欢迎回来！')
```


### 5. 并发编程
```python
import threading
import time

def worker(name):
    print(f"线程 {name} 开始工作")
    time.sleep(2)
    print(f"线程 {name} 完成工作")

# 创建并启动线程
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Worker-{i}",))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()
```


## 🚀 快速开始

### 环境要求
- Python 3.6 或更高版本
- 基础的 Python 环境（无需额外依赖）

### 运行示例
```bash
# 克隆项目
git clone <repository-url>
cd py_learning

# 运行基础示例
python3 "基本数据类型/基本数据类型（字符串）.py"

# 运行面向对象示例
python3 "类/类（多态）.py"

# 运行并发编程示例
python3 "进程与线程/线程（join）.py"
```


## 📖 学习建议

### 🎯 学习顺序推荐
1. **基础语法** - 先掌握变量、数据类型、控制结构
2. **函数编程** - 理解函数定义、参数传递、高阶函数
3. **面向对象** - 学习类的定义、继承、多态等概念
4. **并发编程** - 掌握多线程和多进程编程

### 💡 学习技巧
- 🧪 **动手实践** - 修改代码示例，观察运行结果
- 📝 **做笔记** - 记录重要概念和易错点
- 🔍 **深入理解** - 不仅要会用，还要理解原理
- 🔄 **反复练习** - 多次练习重要概念

## 🛠 技术要点

| 技术领域 | 涵盖内容 |
|---------|---------|
| **基础语法** | 变量、数据类型、运算符、控制结构 |
| **容器类型** | 列表、元组、字典、集合操作 |
| **函数编程** | 参数传递、返回值、匿名函数、闭包、装饰器 |
| **面向对象** | 类定义、继承、多态、封装、元类 |
| **并发编程** | 多线程、多进程、线程同步、进程通信 |
| **高级特性** | 迭代器、生成器、列表推导式 |

## 📊 项目统计

```python
# 项目代码统计（示例）
总计文件数: 30+
总计代码行数: 2000+
涵盖知识点: 50+
```


## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个学习项目！

### 贡献方式
1. 🐛 报告 bug 或提出改进建议
2. ✨ 添加新的代码示例
3. 📝 改进现有代码的注释和文档
4. 🎨 优化项目结构和 README

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

感谢所有为 Python 社区做出贡献的开发者们，以及开源项目提供的灵感和支持。

---

<div align="center">
  <p>🎉 Happy Coding! 🎉</p>
  <p>让学习 Python 变得简单有趣</p>
</div>

---

### 🌈 彩蛋代码

```python
# 有趣的 Python 特性演示
import this  # Python 之禅

# 列表推导式的魔力
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

# 链式比较
a = 5
print(1 < a < 10)  # True

# 交换变量
x, y = 10, 20
x, y = y, x
print(x, y)  # 20 10
```


---

<p align="center">
  <b>如果这个项目对你有帮助，请给它一个 ⭐️</b>
</p>