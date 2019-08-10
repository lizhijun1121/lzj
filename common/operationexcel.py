import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
from xlutils.copy import copy

class OperationExcel(object):
    def __init__(self,filename,index=0):
        """

        :param filename: 文件路径
        :param index: 表的索引
        """
        # 打开excel表文件
        self.filename = filename
        self.table = xlrd.open_workbook(filename=filename)
        # 打开具体的表格
        self.sheet = self.table.sheet_by_index(index)

    def read_excel_data(self):
        # 获取总行数
        rows = self.sheet.nrows
        # 获取总列数
        cols = self.sheet.ncols
        all_data_list = []
        for row in range(1,rows):
            cell_data_list = []
            for col in range(cols):
                cell = self.sheet.cell_value(row,col)# 得到单元个的数据
                ctype = self.sheet.cell(row,col).ctype# 得到数据类型
                if ctype == 2 and cell % 1 == 0:# 说明数据类型是整数
                   cell = int(cell)
                elif ctype == 3:
                    date = datetime(*xldate_as_tuple(cell,0))# 说明数据类型是日期格式
                    cell = date.strftime("%Y_%m_%d %H_%M_%S")
                elif ctype == 4:
                    cell = True if cell == 1 else False# 说明数据类型是布尔值
                cell_data_list.append(cell)
            all_data_list.append(cell_data_list)
        return all_data_list
    def get_data_for_dict(self):
        #将表格的第一行作为字典的键
        keys = self.sheet.row_values(0)
        #将表格中剩余的数据作为字典的值
        values = self.read_excel_data()
        # 准备一个空列表
        data_list = []
        for value in values:
            tmp = zip(keys,value)  # 组成键值对,组合好了以后是一个元祖
            data_list.append(dict(tmp))  # 将得到的组合成的键值对转换成字典并添加到空列表里面
        return data_list

    def write_excel(self,new_data:list):
        """
        1.复制老表格的数据
        2.重新打开复制的表格
        :return:
        """
        #1.复制老表格文件
        new_table = copy(self.table)
        #2.打开新表格
        new_sheet = new_table.get_sheet(0)
        #3.插入新数据--插入一行数据
        insert_row_no = 1 # 将数据从第2行插入
        #获取插入数据的个数
        num = len(new_data)
        for i in range(num):
            new_sheet.write(insert_row_no,i,new_data[i])
        #4.复写老数据
        # 获取老数据的行数
        rows = self.sheet.nrows
        # 获取老数据的列数
        cols = self.sheet.ncols
        for row in range(1,rows):
            for col in range(cols):
                new_sheet.write(row+1,col,self.sheet.cell_value(row,col))
        #5.保存
        new_table .save(self.filename)




if __name__ == '__main__':
    oper = OperationExcel("./data.xls")
    data = oper.get_data_for_dict()
    print(data)