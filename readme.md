

# uwsgi + flask + funboost demo演示，部署应该分为两两次部署

其实不需要这个demo，funboost 和django  flask  fastapi 任意web框架搭配没有任何区别，
但是有的人老是爱问 funboost 怎么和某某web框架搭配，那就写一个项目。

funboost 和django搭配不像 django_celery 还要专门特意搞个三方插件包，完全不需要，在任何web框架中使用funboost都没有需要专门学习的三方插件包。 

# 1 启动消费  
```
cd 到当前项目根目录 uwsgi_flask_funboost
export pythonpath=./

python funboost_funcs.py  # 第一次运行funboost会在项目根目录下生成配置文件 funboost_config.py ，按需修改配置文件的中间件配置。
```

# 2 uwsgi 启动flask web

```
cd 到当前项目根目录 uwsgi_flask_funboost
export pythonpath=./     # 这一步重要，去看 pythonpathdemo  项目 https://github.com/ydf0509/pythonpathdemo

uwsgi --ini uwsgi_conf.ini   

```

# 3 测试url请求

```
在王子中打开  http://192.168.64.151:8011/add?x=4&y=8    # ip是部署uwsgi的服务器的up 端口是uwsgi中配置的端口
```

可以看到接口中发布x=4 y=8 到消息队列中， 后台消费进程会从消息队列中拉取消息运行 4+8

接口中推送消息截图
![img_1.png](img_1.png)

后台消费消息截图
![img.png](img.png)
