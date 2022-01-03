import random

str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
list1 = list(str1)
verification_code = [list1[random.randint(0,len(list1) - 1)] for i in range(4)]
for i in verification_code:
    print(i,end='')