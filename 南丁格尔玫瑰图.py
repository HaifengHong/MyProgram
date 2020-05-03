from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd

data = pd.read_excel('新冠肺炎省份新增.xlsx')
provinces = data['省份'].tolist()
numbers = data['新增人数'].tolist()
colors = data['颜色'].tolist()
print(colors)

# 创建饼图
pie = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))

# 添加数据  # 设置饼图半径、圆心坐标，通过rosetype参数设置展示南丁格尔图
pie.add('', [list(z) for z in zip(provinces, numbers)], radius=['30%', '135%'], center=['50%', '65%'], rosetype='area')

# 设置全局变量（设置标题、不显示图例）
pie.set_global_opts(title_opts=opts.TitleOpts(title='南丁格尔玫瑰图'), legend_opts=opts.LegendOpts(is_show=False))

# 设置系列配置和颜色（设置标签的显示格式、显示位置、字体和大小、饼图颜色等）
pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12, formatter='{b}:{c}天', font_style='italic', font_weight='bold', font_family='Microsoft YaHei'))
pie.set_colors(colors)

# 在网页生成图片
pie.render('南丁格尔玫瑰图.html')
