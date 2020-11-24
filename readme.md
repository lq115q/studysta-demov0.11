### 基于python开发的学习时间统计脚本DEMO-v0.1 by lqq 
#### 注意：运行前需要安装msvcrt及csv库  
    pip install msvcrt -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install csv -i https://pypi.tuna.tsinghua.edu.cn/simple
#### 操作说明：  
1. 输入plan，基于模板制定计划；  
2. 输入start，选择计时学习或输入模块学习时长，统计每日学习情况；  
3. 输入quit，退出  
#### 功能：  
1. 以倒计时的方式，分模块统计每日学习剩余时长；
2. 分模块将学习情况写入文件进行记录；
3. 制定、修改学习计划。
#### 说明：  
1. 剩余学习时间每晚24：00刷新，如需改动，请手动修改tmp.csv最后一行；
2. 时间统计只保留到分钟，秒数自动舍去（占空间且没有太大意义）；
3. 计划只可增加不可减少，否则数据统计会混乱。如需减少计划，请删除临时文件tmp.csv  
#### 发现BUG：
1. 如果修改计划，新增项目的话，读取的还是老项目的时间，然后就会报错(已修复2020/11/24)