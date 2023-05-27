"""
FileName: countAssignmentsV4.0.py
Created time: 2022-12-2 21:42
Last edited time:2023-05-04 11:52
Author: Xinfeng Wu
Function:统计学生作业
Platform: windows 10
Description:

此版本依赖的文件夹目录结构如下所示：

─2021.9-2022.2	//作业文件夹的根目录
    │
    └─61			//班级
        ├─第1周
        ├─第2周
        ├─……
        └─第N周
    └─62
        ├─第1周
        ├─第2周
        ├─……
        └─第N周
    ……
"""
import re
from tkinter import filedialog
import csv
import os

# 以下库用来 将生成的csv文件保存为jpg图片
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontManager
import dataframe_image as dfi
from PIL import ImageFont, ImageDraw, Image


def insert_heading2_img(img_name: str, heading_text: str):
    img = Image.open(img_name)  # 打开图片
    # print(img.mode)
    # 四通道转三通道
    if img.mode == "RGBA":
        img = img.convert('RGB')

    # 创建新图片
    img_new = Image.new('RGB', (img.size[0], img.size[1] + 50), (255, 255, 255))

    draw = ImageDraw.Draw(img_new)  # 读取

    # fnt = ImageFont.truetype('msyh.ttc', 50)  # 设置字体及大小
    fnt = ImageFont.truetype('simhei.ttf', 50)  # 设置字体及大小
    # 标题宽度
    w = draw.textlength(heading_text, font=fnt)
    # print(w)
    #标题 表格居中
    draw.text(((img.size[0]-w) / 2, 0), heading_text, fill='black', font=fnt)  # 写入标题 位置坐标 颜色
    # img_new.show()

    img_new.paste(img, (0, 50))  # 添加到新图片上 x,y 轴参数
    img.close()
    # img_new.show()
    img_new.save(img_name)  # 保存图片
    img_new.close()


semester_path = "D:\\2023.2-2023.7\\Assigments\\"

until_which_week = input("统计截止哪一周?\n")
# which_class = input("Which Class?\n")
all_classes = ['55', '56', '57',  '58', '59', '510',
               '61', '62', '63', '64', '65',
               '66', '67', '68', '69']

# 输出文件（csv，jpg）目录
save_path = semester_path + "统计结果"
if os.path.exists(save_path):
    # 清空
    for root, dirs, files in os.walk(save_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    print(f'文件夹{save_path}已清空！')
else:
    os.mkdir(save_path)
    print(f'文件夹{save_path}已创建！')

for which_class in all_classes:
    studentInfo = "D:\\2023.2-2023.7\\Assigments\\学生信息\\" + which_class + ".csv"
    class_path = semester_path + '\\' + which_class
    # 读入学生信息表
    students_sheet = open(studentInfo, 'r', encoding='gbk')  # 有标题行
    readers = csv.reader(students_sheet, delimiter=',')
    # next(readers)  # 跳过标题行
    # 写入CSV文档
    result_csv = save_path + '\\' + which_class + '班-第1-' + until_which_week + '周-'+'作业统计表.csv'
    read_csv = open(result_csv, 'w', encoding='gbk', newline='')
    writer = csv.writer(read_csv)
    # 标题行
    title ="2023.2-2023.7学年度 " + which_class + '班 第1-' + until_which_week + '周 '+'信息技术作业完成统计表'
    # 列标题行写入
    header = ['编号', '班级', '姓名', '作业类型']
    for i in range(1, int(until_which_week)+1, 1):
        week_col = '第' + str(i) + '周'
        header.append(week_col)
    header.append('实交')
    header.append("应交")
    header.append("缺考")
    header.append("等级")
    writer.writerow(header)

    for (index, which_class, name, assignment_type, absence_time, aquired_time) in readers:  # 遍历学生信息

        row = [index, which_class, name, assignment_type]
        sum_of_until_this_week = 0
        for week in range(1, int(until_which_week)+1, 1):  # 遍历周次
            week_col = '第' + str(week) + '周'
            week_path = class_path + '\\' + week_col
            sum_of_this_week = 0
            if os.path.exists(week_path):
                # for filename in os.listdir(week_path):  # 遍历每个文件
                for root, dirs, filenames in os.walk(week_path):
                    for filename in filenames:
                        # print(filename)
                        # 用于精确匹配，避免例如：周鑫，周鑫磊，张周鑫同时出现在一个班，而导致周鑫被错误统计，但文件名必须要又“姓名-”模式
                        # 适合计算机教室3
                        # pattern = name + "-"
                        pattern = name
                        # 用于精确匹配，避免例如：周鑫，周鑫磊，张周鑫同时出现在一个班，而导致周鑫被错误统计，但文件名必须要又“姓名.”模式
                        # 适合计算机教室1,2
                        # pattern = name+ "."
                        if re.search(pattern, filename):  # 匹配查找
                            sum_of_this_week += 1
                # print(name, sum_of_this_week)

                row.append(sum_of_this_week)  # 追加“第i周”列值
                sum_of_until_this_week += sum_of_this_week
            else:
                row.append("0")  # 追加“第i周”列值为0
                continue
        # 等级计算
        if sum_of_until_this_week >= int(int(aquired_time) * 0.9):
            level = "优秀"
        if int(int(aquired_time) * 0.75) <= sum_of_until_this_week < int(int(aquired_time) * 0.9):
            level = "良好"
        if int(int(aquired_time) * 0.6) <= sum_of_until_this_week < int(int(aquired_time) * 0.75):
            level = "及格"
        if sum_of_until_this_week < int(int(aquired_time) * 0.6):
            level = "待及格"
        row.append(sum_of_until_this_week)  # 追加“总计”列值
        row.append(aquired_time)  # 追加“应交”列值
        row.append(absence_time)  # 追加“缺考”列值
        row.append(level)  # 追加“等级”列值

        writer.writerow(row)
    # print(which_class + "'s csv file gets done!")
    students_sheet.close()
    read_csv.close()

    # 将生成的csv文件保存为jpg图片
    fm = FontManager()
    mat_fonts = set(f.name for f in fm.ttflist)
    # print(mat_fonts)
    plt.rcParams['font.family'] = ['SimHei']
    data = pd.read_csv(result_csv, encoding='gbk')  # 要与生成的csv编码保持一致
    # print(data)

    data_new = data.sort_values(by='实交', ascending=False, ignore_index=True)
    # print(data_new)
    img_name = result_csv.replace('.csv', '.jpg')
    dfi.export(obj=data_new, filename=img_name, fontsize=30, table_conversion="firefox")
    # print(which_class + "'s imagine file gets done!")
    # 插入标题行并合成新图片
    insert_heading2_img(img_name, title)

print("All done!")
# 打开统计结果文件夹
os.startfile(save_path)
