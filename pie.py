import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager


# 指定字体路径
font_path = '鸿雷板书简体-Regular.ttf'  # 替换为实际路径
font_prop = font_manager.FontProperties(fname=font_path)

# 加载数据
df = pd.read_csv('vgsales.csv')

# 对数据的字段进行清理并重新设置索引
data = df.drop(['Rank', 'Year'], axis=1).set_index('Name')

# 计算每种游戏类型的总销量
genre_sales = data.groupby('Genre')['Global_Sales'].sum()

# 创建画布
plt.subplots(figsize=[18, 8])

# 绘制总销售额最大的前5中游戏类型
genre_sales.nlargest(5).plot(kind='pie',
autopct='%1.1f%%',
ylabel='')
plt.title("最受欢迎的5种游戏类型", fontproperties=font_prop)
plt.savefig('pie')  # 保存对比直方图到指定目录，可根据需要修改路径
plt.show()
