class MyDecorator(object):
    def __init__(self,func):
        self.func =func
    def __call__(self, *args, **kwargs):
        print("课上完了")
        self.func()
@MyDecorator
def show():
    print("快要下学了")

if __name__ == '__main__':
    print(dir(show))
    show()


