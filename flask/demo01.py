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



#app初始化简介

'''
DEBUG:是否启用debug模式，默认false。
TESTING :启用/禁止测试模式
SECRET_KEY :密钥,在启用session等很重要
SESSION_COOKIE_NAME :设置保存的session在 cookie 的名称
SESSION_COOKIE_DOMAIN：设置会话的域，默认是当前的服务器，因为Session是一个全局的变量，可能应用在多个app中；设置这个参数必须设置SERVER_NAME,否则报错
PERMANENT_SESSION_LIFETIME：session失效时间，作为一个 datetime.timedelta 对象，也可以用秒表示；
LOGGER_NAME:日志记录器的名称，默认__name__;
SERVER_NAME:服务器的名称以及端口，需要它为了支持子域名 (如: 'myapp.dev:5000')
MAX_CONTENT_LENGTH:设置一个请求所允许的最大的上传数据量，单位字节；
SEND_FILE_MAX_AGE_DEFAULT:  设置调用send_file发送文件的缓存时间；
TRAP_HTTP_EXCEPTIONS:如果这个值被设置为 True ， Flask 不会执行 HTTP 异常的错误处理， 而是像对待其它异常一样，通过异常栈让它冒泡;
PREFERRED_URL_SCHEME:设置URL 模式用于 URL 生成。如果没有设置 URL 模式，默认将为 http 。
JSON_AS_ASCII：默认情况下 Flask 序列化对象成 ascii 编码的 JSON。 如果不对该配置项就行设置的话，Flask 将不会编码成 ASCII 保持字符串原样，并且返回 unicode 字符串。jsonfiy 会自动按照 utf-8 进行编码并且传输。
JSON_SORT_KEYS：默认情况下 Flask 将会依键值顺序的方式序列化 JSON。 这样做是为了确保字典哈希种子的独立性，返回值将会一致不会造成 额外的 HTTP 缓存。通过改变这个变量可以重载默认行为。 这是不推荐也许会带来缓存消耗的性能问题。
JSONIFY_PRETTYPRINT_REGULAR：如果设置成 True (默认下)，jsonify 响应对象将会完美地打印。
'''

#通过配置参数设置参数
'''
app.config.from_pyfile("./config.cfg") # 指定参数的路径，内容按行书写,配置文件放置在与app的同目录下

def from_pyfile(self, filename, silent=False):
    filename = os.path.join(self.root_path, filename)
    pass
'''

#通过类设置参数
'''
class Config(object):  # 该类可以定义在一个py文件中然后导入py文件
    """配置参数"""
    DEBUG = True
app.config.from_object(Config)
通过json格式的文件配置
# config.json
{
    'DEBUG' = True
}
app.config.from_json('config.json') # 配置文件放置在与app的同目录下

直接操作app.config对象进行设置
app.config["DEBUG"] = True
或者
app.config.update({
    "DEBUG":True,
})
'''
@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(debug=True)      # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载

