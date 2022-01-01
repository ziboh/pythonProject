for i in range(3):
    username = input('请输入您的登录账号：')
    password = input('请输入您的登录密码：')
    if username =='admin':
        if password == 'admin888':
            print('恭喜你，登录成功')
            break
        else:
            if i == 2:
                print('错误次数已用完，请退出')

            else:
                print(f'密码错误,您还有{2 - i }次机会，请重新输入')
    else:
        if i == 2:
            print('错误次数已用完，请退出')
        else:
            print(f'输入的账号错误，您还有{2 - i }次机会，请重新输入')
