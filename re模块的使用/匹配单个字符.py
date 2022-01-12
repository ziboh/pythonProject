import re


match_obj = re.match("t.o","two")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("葫芦娃[1234567]","葫芦娃7")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("[0-9]","435344")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("\d","435344")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("\D","324FSD")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


match_obj = re.match("葫芦娃\s[1234567]","葫芦娃 7")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("葫芦娃\s[1234567]","葫芦娃 7")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


match_obj = re.match("[a-zA-Z0-9_]","ha")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("\w","哈")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("\W","【")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("\S","葫芦娃 7")
# print(match_obj)
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


