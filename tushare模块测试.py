"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import tushare as ts
import modin.pandas as pd
import os

def stock_writeto_xls(index):
    """股票获取写入excel中"""
    df = ts.get_hist_data(str(index))

    name = []
    for i in range(df.shape[0]):
        name.append("股票代码："+str(index))
        #name = {'name':name}
    df.insert(0, 'name', name)
    df = df.reset_index()
    path = __file__.split(".")[0]+"\\data"
    if not os.path.exists(path):
        os.makedirs(path)
    writer = pd.ExcelWriter(path+"\\{name}.xls".format(name=index))
    df.to_excel(writer,sheet_name =str(index),index=False)
    print("股票代码：{name}写入成功---------------------------".format(name=index))
    writer.save()
stock_writeto_xls(300120)
def stock_visualization():
    pass