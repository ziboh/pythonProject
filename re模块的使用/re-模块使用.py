import re

# 1、根据正则表达式匹配数据
# 1、正则表达式
# 3、返回匹配对象
match_obj = re.match("he","hello")

result = match_obj.group()
print(result)
