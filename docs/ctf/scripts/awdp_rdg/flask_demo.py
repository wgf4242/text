from flask import Flask, render_template, request, send_from_directory, render_template_string
app = Flask(__name__)
blacklists = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "lipsum", ".", "global", "request", "config",
              "builtins", "%", "~", "'", "_", "os", "cat", "read", "next", "open", "url"]


@app.route('/', methods=['POST', 'GET'])
@app.route('/index.php', methods=['POST', 'GET'])
def Hello():
    return render_template("index.html")

@app.route('/name.php', methods=['POST'])
def Name():
    name = request.form['name']
    for blacklist in blacklists:
        if blacklist in str(name).lower():
            template = '<h2>Good Job %s!</h2>' % "nooo"
            return render_template_string(template)
    template = '<h2>Good Job %s!</h2>' % name
    # template = '<h2>Good Job {{name}}!</h2>' # 修复
    return render_template_string(template, name=name)

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.errorhandler(404)
def miss(e):
    return """
<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 Not Found</h1></center>
<hr><center></center>
</body>
</html>
    """, 404

if __name__ == '__main__':
    app.run(debug="false", host='0.0.0.0', port=8888)