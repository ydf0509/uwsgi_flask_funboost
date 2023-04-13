
import time
from funboost import boost

@boost('uwsgi_add_queue')
def add(x,y):
    print(f'x: {x}   y: {y}')
    time.sleep(10)  # 模拟函数耗时大
    return x+y


if __name__ == '__main__':
    add.consume()