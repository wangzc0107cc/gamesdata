import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager

from scipy.spatial.distance import cdist
# 指定字体路径
font_path = '鸿雷板书简体-Regular.ttf'  # 替换为实际路径
font_prop = font_manager.FontProperties(fname=font_path)

# 加载数据
df = pd.read_csv('vgsales.csv')



# 使用均值填充空缺值
df['Year'] = df['Year'].fillna(int(df['Year'].mean()))

# 创建包含所有年份的数组
years = range(int(df['Year'].min()), int(df['Year'].max()) + 1)

# 使用循环填充空值
for idx, row in df.iterrows():
    if pd.isna(row['Year']):
        # 找到距离最近的年份
        distances = cdist([[row['Year']]], [[year] for year in years], metric='euclidean')
        closest_year = years[distances.argmin()]
        # 填充空值
        df.loc[idx, 'Year'] = closest_year

# 统计每年最畅销的游戏
yearly_sale = df.groupby(['Year']).sum()['Global_Sales']

# 统计各平台每年的总销量
platform_yearly_sale = df.groupby(['Platform', 'Year']).sum()['Global_Sales'].reset_index()

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置图形大小
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=[14, 7])

# 创建一个新的图形和坐标轴
axes[0].plot(yearly_sale.index,yearly_sale)

# 设置标题和标签
axes[0].set_title('游戏每年的总销量', fontproperties=font_prop)
axes[0].set_xlabel('年份', fontproperties=font_prop)
axes[0].set_ylabel('销量', fontproperties=font_prop)

# 旋转x轴标签
plt.setp(axes[0].get_xticklabels(), rotation=45)

# 设置标签旋转角度
plt.xticks(rotation=90)

# 创建字典以存储每个平台的总销量
platform_sale = {}

# 遍历数据的每个分组
for platform, group in platform_yearly_sale.groupby('Platform'):
    platform_sale[platform] = group.set_index('Year')['Global_Sales']

# 遍历字典的每个平台
for platform, sales in platform_sale.items():
    axes[1].plot(sales.index, sales, label=platform)

# 设置标题
axes[1].set_title('不同平台每年的总销量', fontproperties=font_prop)

# 设置x轴标签
axes[1].set_xlabel('年份', fontproperties=font_prop)

# 设置y轴标签
axes[1].set_ylabel('销量', fontproperties=font_prop)

# 自动调整布局
plt.tight_layout()

# 添加图例
axes[1].legend()

plt.savefig('year')  # 保存对比直方图到指定目录，可根据需要修改路径
# 显示图形
plt.show()

