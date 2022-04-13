# ----------------------使用 scatter() 绘制散点图并设置样式-------------------------#
# 要绘制单个点可使用方法 scatter()
# 向它传入一对 x 坐标和 y 坐标，它将在指定的位置绘制一个点
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()

# -----------------------------------------------------------------------------------#
# 下面来设置图标样式，使其更有趣
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
# 参数 s 设置h绘制图形时点的尺寸
ax.scatter(2, 4, s=200)

# 设置图标标题并给其坐标轴加上标签
ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the vlaue", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# ------------------------使用 scatter() 绘制一系列的点-------------------------------#
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the vlaue", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# ----------------------------------自动计算数据-----------------------------------------#
# 使用Pythond 的循环实现
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # 列表解析

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the vlaue", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
# 方法 .axis()
ax.axis([0, 1_100, 0, 1_100_000])

plt.show()

# --------------------------自定义颜色----------------------------#
# 要要修改数据点的颜色，可向 scatter() 传递参数 c，
# 并将其设置为要使用的颜色的名称
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # 列表解析

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
# 参数 c 传入要设置的颜色
ax.scatter(x_values, y_values, c='red', s=10)

ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the vlaue", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1_100, 0, 1_100_000])

plt.show()

# 也可使用RGB颜色模式自定义颜色
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # 列表解析

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
# 参数 c 传入RGB自定义颜色元组数值
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the vlaue", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1_100, 0, 1_100_000])

plt.show()


# -------------------------------使用颜色映射---------------------------------#
"""
     颜色映射: 是一系列颜色，从起始颜色渐变到结束颜色。
     在可视化中，颜色映射用来突出数据的规律。
     例如，你可能使用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。

     要了解 pyplot 中所有的颜色映射:
     可访问 Matplotlib 网站主页(https://matplotlib.org/),单击Examples,向下滚动
     到 Color，再单击 Colormaps reference

"""
# 如何根据每个点的 y 值来设置其颜色:
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # 列表解析

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
# 将参数 c 设置成了一个 y 值列表，并用参数 cmap 告诉 pyplot 使用哪个颜色映射
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the vlaue", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1_100, 0, 1_100_000])

plt.show()

# ------------------------自动保存图表--------------------------- #
"""
    要让程序自动保存图表到文件，可将调用plt.show() 替换为调用 plt.savefig()
"""
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # 列表解析

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
# 将参数 c 设置成了一个 y 值列表，并用参数 cmap 告诉 pyplot 使用哪个颜色映射
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the vlaue", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1_100, 0, 1_100_000])

plt.savefig('squares_plot.png', bbox_inches='tight')
# 第一个实参指定要以什么文件名保存图表，文件将默认存储到该py文件同目录下
# 第二个实参指定将图表多余的空白区域裁剪掉，如果要保留空白区域，省略该实参即可