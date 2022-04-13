# ------------------------模拟多次随机漫步---------------------- 3
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断模拟随机漫步。
while True:
	# 创建一个RandomWalk的实例
	rw = RandomWalk()
	rw.fill_walk()

	# 将所有的点都绘制出来
	plt.style.use('seaborn-dark')
	fig, ax = plt.subplots()
	ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues, s=15)
	plt.show()

	keep_running = input("Make another walk?(yes/no): ")
	if keep_running == 'no':
		break
