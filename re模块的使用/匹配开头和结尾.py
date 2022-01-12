import re

match_obj = re.match("^\d.*","1adc")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配错误")

match_obj = re.match(".*\d$", "1")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配错误")



match_obj = re.match("^\d.*\d$", "1fwqfqw2fds4")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配错误")


match_obj = re.match("[^aufo]{1,5}.*", "1xfqfqw2fds4")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配错误")