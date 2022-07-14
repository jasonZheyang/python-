import csv
from pyecharts import options as opts
from pyecharts.charts import  Timeline, Grid, Bar
def createBar(dsDay):
    # 创建柱状图
    dsDay =dsDay[::-1]
    bar = Bar(init_opts=opts.InitOpts(width='1000px', height='2500px'))
    # 柱状图数据及参数设置
    bar.add_xaxis([x for x, y in dsDay])
    bar.add_yaxis("nba球人员薪资（万美元）",
                  [y for x, y in dsDay],
                  category_gap="60%",
                  color='red',
                  itemstyle_opts={'normal': {'opacity': 0.8}})
    bar.set_series_opts(label_opts=opts.LabelOpts(
        position="right"))
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=False, max_=5000),yaxis_opts=opts.AxisOpts(is_show=True,axislabel_opts=opts.LabelOpts()),
            title_opts=opts.TitleOpts(title="nba球人员薪资（万美元）",

                                      title_textstyle_opts=opts.TextStyleOpts()),
            visualmap_opts=opts.VisualMapOpts(is_show=True,pos_right="10px",
                                                max_=5000, is_piecewise=False,
                                                 dimension=0, range_color=['#6495ED', '#00FF00', '#FFFF00', '#808000',
                                                                        '#808000', '#FF0000', '#FF0000', '#000000','#000000']))
    bar.reversal_axis()
    return bar
timeLine = Timeline(init_opts=opts.InitOpts(width='1000px'))

for i in range(2011,2022):
    csv_reader = csv.reader(open(f"薪资{i}.csv"))
    dataCovid = list(csv_reader)

    playername = []
    for j in range(1, len(dataCovid)):
        playername.append((str(dataCovid[j][0])))


    nbasalary = []  # 确诊数字
    for j in range(1,len(dataCovid)):
        nbasalary.append(int(dataCovid[j][1]))

    dsDay = list(zip(playername, nbasalary))
    dsDay.sort(key=lambda x: x[1], reverse=True)
    m = []
    m.append(createBar(dsDay))
    for n in m:
        timeLine.add(n, str(i))
    # 时间线参数设置
    timeLine.add_schema(play_interval=100, is_auto_play=False,
                        is_loop_play=False, symbol_size=5,pos_bottom="5px")
# 绘制时间线
timeLine.render('NBAtimeLine.html')#render 绘制




