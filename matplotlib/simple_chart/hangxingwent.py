import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 设置图表样式:
plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Number", fontsize=17)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("The square of the value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()