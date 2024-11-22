import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
df = pd.read_csv('vgsales.csv')


# 设置图片清晰度
plt.rcParams['figure.dpi'] = 600


# 主图宽高和子图布局
fig, axes = plt.subplots(ncols=3, nrows=1, figsize=[18, 6])

# 筛选出每个地区最畅销的5种游戏类型，颜色依次为红、橙、黄、绿、青
na_top_genres = df.groupby('Genre').sum().nlargest(5, 'NA_Sales').reset_index()
na_top_genres['Region'] = 'NA'

eu_top_genres = df.groupby('Genre').sum().nlargest(5, 'EU_Sales').reset_index()
eu_top_genres['Region'] = 'EU'

jp_top_genres = df.groupby('Genre').sum().nlargest(5, 'JP_Sales').reset_index()
jp_top_genres['Region'] = 'JP'

top_genres = pd.concat([na_top_genres, eu_top_genres, jp_top_genres])
for i, region in enumerate(top_genres['Region'].unique()):
    region_data = top_genres[top_genres['Region'] == region]
    axes[i].bar(region_data['Genre'], region_data['Global_Sales'], color=['red', 'orange', 'yellow', 'green', 'cyan'])

    # 设置子图标题
    axes[i].set_title(f'{region} Top 5 best-selling game types in the region')

plt.savefig('column')  # 保存对比直方图到指定目录，可根据需要修改路径
plt.show()