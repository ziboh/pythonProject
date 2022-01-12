# * 	    匹配前一个字符出现0次或者无限次，即可有可无
# + 	    匹配前一个字符出现1次或者无限次，即至少有1次
# ? 	    匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m} 	    匹配前一个字符出现m次
# {m,n} 	匹配前一个字符出现从m到n次

import re

match_obj = re.match("t.*o","tfdsfdsfdsdsxfso")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


match_obj = re.match("t.+o","tfdsfsdofdsfds")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("https?","httpsd")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


match_obj = re.match("ht{1,3}ps?","htttpsd")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")