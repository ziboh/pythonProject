# 使用Python打印直线
def line(nums,len):
    for i in range(nums):
        print('-' * len)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

while True:
    len = input('输入横线长度：')
    nums = input('输入横线数量：')
    if is_number(len) and is_number(nums):
        nums = int(nums)
        len = int(len)
        line(nums,len)
        break
    else:
        print('请输入数字')
