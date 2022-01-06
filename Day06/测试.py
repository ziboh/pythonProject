# def func(c):
#     a = ["Movie(", "'", c, "'", ")"]
#     b = ''.join(a)
#     print(b)
#
# f = 'cawd-185'
# func(f)
zhou = {"Movie('cawd-185')":123,"Movie('cawd-111')":862}
chou = {}
for i ,j  in zhou.items():
    j = i
    i = i.replace("'", "")
    i = i.replace("(", "")
    i = i.replace(")", "")
    i = i.replace("Movie", "")
    print(i)
    print(j)
    chou [i] = zhou [j]
    # zhou[i] = zhou.pop(j)
print(chou)