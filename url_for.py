# This code shows the dynamic URL building of a web application.

from flask import Flask, url_for,redirect
app = Flask(__name__)

@app.route('/admin')
def Hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def Hello_guest(guest):
    return 'Hello %s as Guest' %guest

@app.route('/user/<name>')
def Hello_user(name):
    if name=='admin':
        return redirect(url_for('Hello_admin'))
    else: 
        return redirect(url_for('Hello_guest',guest=name))

if __name__ == '__main__':
    app.run(debug=True)