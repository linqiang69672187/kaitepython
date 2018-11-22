# encoding:utf-8
from flask import Flask,render_template,request #创建Flask程序实例
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import required
app = Flask(__name__)    #创建Flask程序实例,模块主程序或者包名称


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/',methods=['GET','POST'])
def index():
     username = request.form['name']
     retxt=''
     if username=='林强':
         retxt='[{"name":"aa'+username+'"}]'
     else:
         retxt ='[{"name":"'+username+'"}]'

     return retxt

@app.route('/user/<name>')
def heil(name):
    name = "你好"+name
    return  render_template('user.html',name=name)

if __name__ =='__main__':
    app.run(host="127.0.0.1",port=9000,debug=True)
