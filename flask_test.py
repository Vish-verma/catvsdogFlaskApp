from flask import Flask,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hello/<name>')
def hello_name(name):
    return "hello %s!" % name
@app.route('/hello_admin')
def hello_admin():
    return "hello Admin"

@app.route('/blog/<int:postId>')
def show_blog(postId):
    return  "Blog Number %d" % postId

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' %revNo

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello',name = name))


@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))
if __name__ == '__main__':
    app.run(debug=True)