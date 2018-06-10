#-*- encoding=UTF-8 -*-
__author__ = 'ruihe'

import os
import time
from flask import Flask, request, redirect, url_for,render_template

app = Flask(__name__)
UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file_dir=os.path.join(basedir,app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        f = request.files['photo']
        fname=f.filename
        ext = fname.rsplit('.',1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename=str(unix_time)+'.'+ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir,new_filename))  #保存文件到upload目录
    return "ok"

def valid_login(username,password):
    if(username == ''or password == ''):
        return False;
    return True

def log_the_user_in(username):
    return "Welcome!" + username


if __name__ == '__main__':
    app.run(debug=True)

