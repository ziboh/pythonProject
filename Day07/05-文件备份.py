def bak(file_name):
    new_file = open(file_name.replace('.','[备份].'),'w',encoding='utf-8')
    old_file = open(file_name,'r',encoding='utf-8')
    while True:
        text = old_file.read(10)
        if text:
            new_file.write(text)
        else:
            new_file.close()
            old_file.close()
            print(f'{file_name}备份完毕')
            break
file_name = input('请输入要备份的文件名:')
bak(file_name)