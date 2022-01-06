import functools

def func(n):
    return n ** 2



def funcA(n,m):
    return n * m


def funcB(n):
    return n % 2 == 0

list1 = [1,2,3,4,5]
list2 = list(map(func,list1))
sums = functools.reduce(funcA,list2)
print(sums)
print(list2)

print(type(funcB(1)))
print(list(filter(funcB,list2)))
print(type(filter(funcB,list2)))