from flask import Flask,render_template,request,redirect,flash,url_for
from flask_login import LoginManager,login_required,login_user,current_user
from moudle import User


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'



login_manager=LoginManager(app)
login_manager.session_protection='strong'
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#登陆
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.values.get('username')
        passwd = request.values.get('passwd')
        user=User.query.filter_by(LOGIN_NAME=username,PASSWORD=passwd).first()
        if user is not None:
            login_user(user)
            return redirect(request.args.get('next') or url_for('task.task_adder'))
        flash('用户名或密码错误','loginfail')
    return render_template('index_login.html')

#目录
@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


#任务相关
from task import task
app.register_blueprint(task,url_prefix='/task')



#网签相关
from onlinesign import onlinesign
app.register_blueprint(onlinesign,url_prefix='/onlinesign')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)
