"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import tushare as ts
import pandas as pd
import os,glob
import pandas as pd
import plotly.express as px
import plotly.offline as py


class Stock_make():
    """股票数据获取及其可视化"""
    def __init__(self,input_files,output_file):
        self.input_files=input_files.strip('\u202a')
        self.output_file = output_file.strip('\u202a')

    def stock_writeto_xls(index):
        """股票获取写入excel中"""
        df = ts.get_hist_data(str(index))
        df = df.sort_index()

        name = []
        for i in range(df.shape[0]):
            name.append("股票代码：" + str(index))
            # name = {'name':name}
        df.insert(0, 'name', name)
        df = df.reset_index()
        path = __file__.split(".")[0] + "\\data"
        if not os.path.exists(path):
            os.makedirs(path)
        writer = pd.ExcelWriter(path + "\\{name}.xls".format(name=index))
        df.to_excel(writer, sheet_name=str(index), index=False)
        print("股票代码：{name}写入成功---------------------------".format(name=index))
        writer.save()


    def cancat_excel(self,input_files, outputfiles):
        """数据合并"""
        all_workbook = glob.glob(os.path.join(input_files, '*.xls'))
        data_frames = []
        '''重点来了，遍历工作簿、工作表，簿为列表，表为字典'''
        for workbook in all_workbook:
            all_sheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
            for worksheet_name, data in all_sheets.items():
                data_frames.append(data)
        all_data = pd.concat(data_frames, axis=0, ignore_index=True)
        # axis为列合并，而axis为1则为横向合并

        writer = pd.ExcelWriter(outputfiles)
        all_data.to_excel(writer, sheet_name='30477-30287', index=False)
        writer.save()
        print("数据合并成功--------------------------------------------------------")


    def stockdata_visualization(self,index_x,index_y,index_year):
        """数据可视化"""
        df = pd.read_excel(self.output_file)

        fig = px.bar(df, x=index_x, y=index_y, animation_frame=index_year, color=index_x)

        # fig["layout"].pop("updatemenus") # optional, drop animation buttons
        fig.show()
        py.plot(fig)
        print("数据可视化成功")

