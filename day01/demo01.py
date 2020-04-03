from flask import Flask

app = Flask(__name__)

#app初始化简介
'''
# Flask实例的源码：
class Flask(_PackageBoundObject):
    def __init__(self, import_name,  # 指定应用的名字和工程目录，默认为__name__
                static_path=None,  #  是静态文件存放的路径，会赋值给static_url_path参数
                static_url_path=None,  # 设置静态文件路由的前缀，默认为“/static”
                static_folder='static', # 静态文件的存放目录， 默认值为"static"
                template_folder='templates', # 模板文件的存放目录，默认值为"templates"
                instance_path=None, # 设置配置文件的路径，在instance_relative_config=True情况下生效
                instance_relative_config=False # 设置为True表示配置文件相对于实例路径而不是根路径
                root_path=None) # #  应用程序的根路径
'''

'''
app.run(host=None, # 设置ip，默认127.0.0.1
        port=None, # 设置端口，默认5000
        debug=None)  # 设置是否开启调试，默认fals
'''

@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(debug=True)      # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载

