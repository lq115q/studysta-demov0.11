#!python
#!python3
# -*- coding: UTF-8 -*-

#自动统计学习时长的python脚本
#我想要有的功能：显示剩余学习时间；将学习记录写入文档；能够以图表形式显示学习记录；倒计时功能
#用一个csv保存时间与时间点，每天一行，生成条形图
#用一个md保存时间与时间点，每天一块，详细记录

import time
import os
import msvcrt
import csv

#计时模块
def timer():
    while 1:
        commnd = input('输入start开始，输入quit返回：')
        if commnd == 'start':
            print('计时开始！按下‘q’停止计时！\n')
            break 
        elif commnd == 'quit':
            return 0
        else:
            print('输入错误，请重新输入！')
            continue
    time_start = time.time()
    while 1:
        time.sleep(1)
        time_stop = time.time()
        secend = round(time_stop - time_start)
        minute = secend//60
        minute_out = (secend//60)%60
        hour = minute//60
        secend = secend%60
        print('\r你已经学习了：','{:0>2d}:{:0>2d}:{:0>2d}'.format(hour,minute_out,secend),end='',flush=True)
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 113:
                print('\n计时结束！\n')
                print('你的本次学习时间为：{:0>2d}:{:0>2d}:{:0>2d}'.format(hour,minute_out,secend))
                return minute
#显示学习计划
def show_plan(filename):
    study_part_text = []
    flag = 0
    with open(filename,encoding='utf-8') as file_read:
        f = file_read.readlines()
        print('\n你的学习计划如下：\n')
        for i in f:
            print(i)
        print('=======================================================')
#创建/修改学习计划
def creat_plan():
    note = '## 模块时长：(请输入整数)(可复制整行在其后添加模块<需保持格式不变>)  \n* 模块0时长：90  \n* 模块1时长(min)：180  \n* 模块2时长(min)：180  \n* 模块3时长(min)：180  \n## 学习模块及顺序:  \n0. 英语单词  \n1. 微机原理——数据结构——PYTHON网页——LEETCODE  \n2. pytorch——机器学习——西瓜书——深度学习吴恩达  \n3. 计算机网络——鸟哥的LINUX私房菜  \n'
    if os.path.exists('plan.md'):
        print('你已经有学习计划了，现在进行修改！')
        os.system('notepad plan.md')
    else :
        print('你还没有学习计划，请对模板进行修改！')
        with open('plan.md','a',encoding='utf-8') as file_write:
            file_write.write(note)
        os.system('notepad plan.md')
#学习计划的开始模块
def start_plan():
    time = []
    with open('plan.md',encoding='utf-8') as obj:
        f=obj.readlines()
        for i in f:
            if '*' in i:
                _,num=i.split('：',1)
                num = int(num)
                time.append(num)
    return time
#学习计划的实时完成情况
def write_file(times,writefilename,study_note):
    times_len = len(times)
    if os.path.exists('tmp.csv'):
        with open('tmp.csv',encoding='gbk') as obj:
            f = csv.reader(obj)
            rows = [row for row in f]
            now_date = time.strftime("%Y-%m-%d", time.localtime())
            if rows[-1][0] == now_date:
                for i in range(len(rows[-1])-5):
                    times[i] == (int(rows[-1][5+i]))
        print('欢迎回来，今天剩余学习时间为：')
    else:
        print('欢迎开始今天的学习任务，今天的学习剩余时间为：')
    for i in range(len(times)):
        if times[i] <= 0:
            times[i] = 0
            print('模块{}已完成学习！'.format(i))
        else :
            print('模块{}剩余学习时长：'.format(i) + str(times[i]) +' min')
    while 1:
        study_part = input('\n请输入你完成的模块：')
        if study_part == 'quit':
            break
        time_label_list = [str(i) for i in list(range(len(times)))]
        if study_part not in time_label_list:
            print('输入错误，请重新输入！')
            continue
        study_part = int(study_part)
        timer_need = input('\n是否需要计时学习(Y/N)：')
        if timer_need == 'Y':
            study_time = timer()
        elif timer_need == 'N':
            study_time = input('\n请输入你完成的时长（min）：')
            if not study_time.isnumeric():
                print('输入错误，请输入数字！')
                continue
            study_time = int(study_time)
            if not 0<study_time<300 :
                print('输入错误，请重新输入！')
                continue
        else:
            print('输入错误，请重新输入！')
            continue
        text_note = input('\n请输入你完成的内容：')
        with open(study_note,'a',encoding='utf-8') as file_write:
            file_write.write((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            file_write.write('\t学习模块：'+str(study_part)+'，学习时长：'+str(study_time)+'min，学习内容：'+text_note+'\n')
        print('\n当前学习情况已记录，剩余学习时长为：')
        times[study_part] = times[study_part] - study_time
        flag = 0
        for i in range(len(times)):
            if times[i] <= 0:
                times[i] = 0
                print('模块{}已完成学习！'.format(i))
            else :
                print('模块{}剩余学习时长：'.format(i) + str(times[i]) +' min')
                flag += 1
        with open('tmp.csv','a',encoding='gbk') as file_write:
            file_write.write((time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime())))
            file_write.write(','+str(study_part)+','+str(study_time)+','+text_note)
            file_write.write(''.join([(','+str(time_item)) for time_item in times]))
            file_write.write('\n')
        if flag == 0 :
            print('恭喜你已完成今天的学习任务！')
            break
if __name__ == "__main__":
    hello='===========欢迎来到谦谦的学习统计脚本DEMO-v0.1===========\n\n提示：\n\t输入plan制定/修改你的学习计划\n\t输入start开始你的学习\n\t输入fig生成当前学习情况统计\n\t输入quit退出脚本\n'
    guide='请输入你要做什么：'
    print(hello)
    print('注意：\n\t请预先安装msvcrt及csv库！\n')
    print('=========================================================\n')
    while 1:
        choice = input(guide)
        if choice == 'plan':
            creat_plan()
        elif choice == 'start':
            if os.path.exists('plan.md'):
                times = start_plan()
                show_plan('plan.md')
                write_file(times,'计划统计.md','学习记录.md')
            else :
                print('你还没有学习计划，请重新输入！')
                continue
        elif choice == 'quit':
            break
        elif choice == 'fig':
            print('该功能还在开发中！')
        else:
            print('请检查你的输入是否正确！')
            continue
    
