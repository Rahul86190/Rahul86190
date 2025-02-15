from flask import Flask, url_for,redirect,render_template,request
app = Flask(__name__)

@app.route('/')
def FrontForm():
    return render_template('form.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return user
    else:
        user=request.args.get('email')
        return user
if __name__ == '__main__':
    app.run(debug=True)