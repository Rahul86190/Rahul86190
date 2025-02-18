''' What is a session ?
A session is a way to store information (in variables) to be used across multiple pages.
Unlike a cookie, the information is not stored on the users computer. Session variable is stored on the server itself
'''

''' How does it work ?
When a session is created, a session ID is assigned to the user. The session ID is stored in a cookie.
The session ID is passed back to the server for validation when the user makes another request.
The server uses the session ID to fetch the session information.
'''
from flask import Flask, url_for,redirect,render_template,request,session
app = Flask(__name__)
app.secret_key="any random string you can use" # This is used to encrypt the session data stored on the server. For example: session['name'] = 'username'

@app.route('/')
def FrontForm():
    if 'name' and 'email' in session:
            name = session['name']
            email = session['email']
            return '<h1> Welcome '+name+' You are successfully Login by using session variable information <br><a href ="/logout">click here to logout </a>/h1>'
    return '<h1> Invalid User.<a href="/login">Click here to login</a> </h1>'


@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('FrontForm'))
    return render_template('Session_form_login.html')

@app.route('/logout')
def logout():
    session.pop('name',None)
    session.pop('email',None)
    return redirect(url_for('FrontForm'))

if __name__ == '__main__':
    app.run(debug=True)