# file_name =input('请输入你要上传文件的名称：')
# print(file_name[:file_name.find('.')])
# print(file_name[file_name.find('.'):])
# print(file_name.count('z',0,10))
plies_number = int(input('请输入需要打印的三角形层数：'))
for i in range(1,plies_number + 1):
    print(" " * (plies_number-i),end='')
    print('*' * (2*i-1))


