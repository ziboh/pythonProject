# 导入模块
import os
import shutil

# # 调用rmdir删除空目录
# shutil.rmtree('123')
# os.mkdir('static')

# 创建文件
os.chdir('static')
for i in range(1,4):
    file_name = 'file' + str(i) + '.txt'
    f = open(file_name,'w',encoding='utf-8')



