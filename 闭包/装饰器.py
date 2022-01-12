
def decorator(func):
    def inner(a):
        print('已添加登录验证',a)
        func()
    return inner

@decorator
def comment():
    print("发表评论")



if __name__ == '__main__':
    comment('123')