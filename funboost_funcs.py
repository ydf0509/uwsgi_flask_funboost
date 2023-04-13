

from funboost import boost

@boost('uwsgi_add_queue')
def add(x,y):
    print(f'x: {x}   y: {y}')
    return x+y


if __name__ == '__main__':
    add.consume()