from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd

from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


data = pd.read_excel('D:\PythonCodes\MyPrograms\Pyecharts\规划月刊\广东省2020年1月-6月\广东省2020年1月-6月累计供电量数据\广东省2020年1月-6月累计供电量数据.xlsx')
provinces = data['供电局'].tolist()
numbers = data['累计供电量平方根（亿千瓦时）'].tolist()
colors = data['颜色'].tolist()

pie = Pie(init_opts=opts.InitOpts(width='1000px', height='1500px', page_title='广东省2020年1月-6月累计供电量', bg_color='white'))

pie.add('', [list(z) for z in zip(provinces, numbers)], radius=['30%', '115%'], center=['40%', '50%'], rosetype='radius')

pie.set_global_opts(title_opts=opts.TitleOpts(title='广东省2020年1月-6月累计供电量平方根（亿千瓦时）', pos_left='25%', pos_top='5%'), legend_opts=opts.LegendOpts(is_show=False, pos_top='12%', pos_left='12%', orient='vertical', align='auto'))

# pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12, formatter='{b}:{c}', font_family='Microsoft YaHei'))
pie.set_series_opts(label_opts=opts.LabelOpts(is_show=False, position='inside', font_size=12, font_family='Microsoft YaHei'))
pie.set_colors(colors)

# pie.render('广东省2020年1月-6月累计供电量平方根（radius）.html')

make_snapshot(snapshot, pie.render(), "广东省2020年1月-6月累计供电量平方根（radius）.png", pixel_ratio=13, is_remove_html=True)
