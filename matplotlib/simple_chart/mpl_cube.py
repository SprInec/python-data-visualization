# ------------------------------立方------------------------------ #
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=50)

ax.set_title("Cube Number", fontsize=17)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("The cube of the vlaues", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 5000, 0, 125_000_000_000])

plt.show()