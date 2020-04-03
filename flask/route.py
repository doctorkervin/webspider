from flask import Flask
from urllib import request
from werkzeug.utils import secure_filename

app = Flask(__name__)
'''
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):   # 函数参数中接收传递的参数
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
'''



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['userid'])  # 获取post穿过来的参数
        dict = request.form.to_dict()  # 将请求参数解析成字典
        print(dict['userid'])
        return 'POST'
    else:
        print(request.args['userid'])   # 获取get传过来的参数
        dict = request.args.to_dict()  # 将请求参数解析成字典
        print(dict['userid'])
        return 'GET'


# 获取上传文件
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))

# 返回字典
from flask import jsonify
@app.route('/test', methods=['GET', 'POST'])
def test():
	dict={'a':'a','b':'aaa'}
	return jsonify(dict)

# 返回模版
from flask import render_template
@app.route('/test', methods=['GET', 'POST'])
def test():
	return render_template('index.html',name='aaa')  # 可以向模板传递参数
if __name__ == '__main__':
    app.run(debug=True)  # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
