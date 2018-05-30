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
def hello_world():
   return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)

