from flask import  Flask,render_template #创建Flask程序实例

app = Flask(__name__)    #创建Flask程序实例,模块主程序或者包名称

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def heil(name):
    return  render_template('user.html',name=name)

if __name__ =='__main__':
    app.run(host="127.0.0.1",port=9000,debug=True)
