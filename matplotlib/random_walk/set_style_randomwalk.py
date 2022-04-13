# -----------------------------设计随机漫步图的样式-------------------------- #
# 给点着色
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# 创建一个 RandomWalk 实例
	rw = RandomWalk()
	rw.fill_walk()

	# 将所有的点都绘制出来
	plt.style.use('seaborn-dark')
	fig, ax = plt.subplots()
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c = point_numbers,
		 cmap = plt.cm.Blues, edgecolors='none', s=15)
	plt.show()

	keep_running = input("Make another walk?(y/n): ")
	if keep_running == 'n':
		break
