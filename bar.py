import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager


# 指定字体路径
font_path = '鸿雷板书简体-Regular.ttf'  # 替换为实际路径
font_prop = font_manager.FontProperties(fname=font_path)
# 加载数据
df = pd.read_csv('vgsales.csv')


# 计算市场占有率top5的出版商
publisher_global_sales = df.groupby('Publisher')['Global_Sales'].sum()
publisher_global_sales_top5 = publisher_global_sales.nlargest(5)

# 筛选出市场占有率最高的前5出版商的数据
publisher_top5 = df[df['Publisher'].isin(publisher_global_sales_top5.index)]

# 计算每个出版商在不同地区的市场占有率
publisher_sales_by_region = publisher_top5.groupby('Publisher')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

# 创建画布
fig, axes = plt.subplots(2, 1, figsize=(15, 15))

# 绘制全球数据的柱形图
axes[0].bar(publisher_global_sales_top5.index, publisher_global_sales_top5.values)

# 设置标题和轴标签
axes[0].set_title('全球最受欢迎的5个游戏发行商',fontproperties=font_prop)
axes[0].set_xlabel('发行商',fontproperties=font_prop)
axes[0].set_ylabel('全球总销售额',fontproperties=font_prop)



# 绘制不同地区的柱状图
publisher_sales_by_region.plot(kind='bar', ax=axes[1])
axes[1].set_xlabel('不同类型游戏的发行商',fontproperties=font_prop)
axes[1].set_ylabel('地区总销售额 ',fontproperties=font_prop)
axes[1].set_title('地区性最受欢迎的五个游戏发行商',fontproperties=font_prop)

plt.savefig('bar')  # 保存对比直方图到指定目录，可根据需要修改路径
plt.show()