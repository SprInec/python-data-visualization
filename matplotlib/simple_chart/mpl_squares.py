# ---------------------------绘制简单的折线图--------------------------#
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()

# ---------------------------标签文字和线条粗细-------------------------#
"""
     plot(squares, linewidth):
         参数 linewith 决定了 plot() 绘制的线条粗细

     方法 set_title() 给图表指定标题

     参数 fontsize 指定图表中各种文字的大小

     方法 set_xlabel() 和 set_ylabel() 给每条轴设置标题

     方法 tick_params(axis='both', labelsize=n) 设置刻度样式
         参数 labelsize 设置刻度字号

"""
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# 函数 subplots() 可在一张图片中绘制一个或多个图表
# 变量 fig 表示整张图片
# 变量 ax 表示图片中的各个图表
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签
# 标签最好使用英文，以防出现文字显示问题
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()

# ---------------------矫正图形---------------------------- #
import matplotlib.pyplot as plt

# 为避免图表数据错误，可向 plot() 同时提供输入值和输出值
# 设定输出值
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
# 输出
ax.plot(input_values, squares, linewidth=3)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()