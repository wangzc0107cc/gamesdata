import pandas as pd
import matplotlib.pyplot as plt
# 加载数据
df = pd.read_csv('vgsales.csv')

print('数据基本信息：')
df.info()

print('数据的前几行：')
print(df.head())


# 处理缺失值，直接删除包含缺失值的行，后续如有更复杂的缺失值处理需求可调整
dff = df.dropna()

print('数据的基本信息：')
dff.info()
print('数据的前几行：')
print(dff.head())

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置中文字体
plt.rcParams['font.family'] = ['WenQuanYi Zen Hei']