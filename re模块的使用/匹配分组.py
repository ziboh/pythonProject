# | 	匹配左右任意一个表达式
# (ab) 	将括号中字符作为一个分组
# \num 	引用分组num匹配到的字符串
# (?P<name>) 	分组起别名
# (?P=name) 	引用别名为name分组匹配到的字符串
import re

fruit_list = ["apple","banana","orage","pear","peach"]

for fruit in fruit_list:
    match_fruit = re.match('banana|pear',fruit)
    if match_fruit:
        print(f'我喜欢吃的水果:{match_fruit.group()}')
    else:
        print(f"我不喜欢吃的水果：{fruit}")


email = 'hello@qq.cn'
email_match = re.match("([0-9a-zA-Z_]{4,20})@(163|126|qq)\.(com|cn)",email)
if email_match:
    print(f'正确的邮箱:{email_match.group()}')
    result = email_match.group(3)
    print(result)
else:
    print(f"错误的邮箱：{email_match}")

qq = 'qq:3014587'
qq_match = re.match("qq:([1-9]\d{4,11})",qq)
if qq_match:
    print(f'正确的qq:{qq_match.group(1)}')
else:
    print(f"错误的qq：{qq_match}")

html = "<html>hh</html>"

html = "<html>hh</html>"
html_match = re.match("<([a-zA-Z1-6]+)>.*</\\1>",html)
if html_match:
    print(f'html标签:{html_match.group()}')
else:
    print(f"匹配错误")

# <html><h1>www.itcast.cn</h1></html>
html = "<html><h1>www.itcast.cn</h1></html>"
html_match = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>(.*)</(?P=name2)></(?P=name1)>",html)
if html_match:
    print(f'html标签:{html_match.group(3)}')
else:
    print(f"匹配错误")