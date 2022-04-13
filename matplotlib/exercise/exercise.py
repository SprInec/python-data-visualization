# 分子运动
import matplotlib.pyplot as plt

from randomwalk import RandomWalk

# 增加点数
rw = RandomWalk(5_000)
rw.fill_walk()

plt.style.use('seaborn-dark')
# 调整尺寸
fig, ax = plt.subplots(figsize=(10,6), dpi=128)
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=3)


# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False) 


# 突出起点和终点
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
	 edgecolors='none', s=100)

plt.show()