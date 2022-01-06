# str1 = '1.2.3.4.5.4.6.32.4.kh.k'

def func1():
    # str1 = '1.2.3.4.5.4.6'
    str2 = str1[::-1]
    print(str2.replace('.', '-'))


str1 = '1.2.3.4.5.4.6.32.4.kh.k'
func1()
print(str1)

c1 = 'das'
c2 = 'dad'
c2 ,c1  = c1 , c2
print(c1,c2)
