from flask import Flask, request
from funboost_funcs import add

app = Flask(__name__)


@app.route('/')  # 匹配路由
def hello():
    return "Hello World"


@app.route('/add')
def add_api():
    x = request.args.get('x', type=int)
    y = request.args.get('y', type=int)
    add.push(x, y)
    return 'finish'


if __name__ == '__main__':
    app.run(debug=True)
