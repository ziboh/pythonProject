def verification_code(length):
    import random
    str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    list1 = list(str1)
    verification_code = [list1[random.randint(0,len(list1) - 1)] for i in range(length)]
    nums = ''
    for i in verification_code:
        nums += i
    return nums



print('-' * 40)
print(verification_code(8))