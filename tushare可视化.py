"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import pandas as pd
import plotly.express as px
import plotly.offline as py

df = pd.read_excel(r"J:\PyCharm项目\package_test_\tushare模块测试\excel合并.xls")
df= df.sort_index()

fig = px.bar(df,x="name",y="open", animation_frame="date",color="name")

#fig["layout"].pop("updatemenus") # optional, drop animation buttons
fig.show()
py.plot(fig)