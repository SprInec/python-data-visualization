import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Part1 分析CSV文件头
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
# Part2 打印文件头及其位置
    for index, column_header in enumerate(header_row):
        print(index, column_header)
# Part3 提取并读取数据
    # 从文件中读取日期，最高温度，最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# print(highs)

# 根据最高温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows,  c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
ax.set_title("2018 year the everyday highest weather", fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("temprotuce (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
