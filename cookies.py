# What are cookies?
''' Cookies are data, stored in small text files, on your computer. 
When a web server has sent a web page to a browser, the connection is shut down, and the server forgets everything about the user. 
Cookies were invented to solve the problem "how to remember information about the user":'''

from flask import Flask, url_for,redirect,render_template,request,make_response
app = Flask(__name__)

@app.route('/')
def FrontForm():
    return render_template('cookie_form.html')

@app.route('/Cookie_Set',methods = ['POST', 'GET'])
def Cookie_Set():
    if request.method == "POST":
        user = request.form['name']
        resp=make_response(render_template('get_cookie.html'))
        resp.set_cookie('userName',user)
        return resp
        
    else:
        username=request.args.get('email')
        return username
@app.route('/Cookie_Get')
def Cookie_Get():
    name=request.cookies.get('userName')
    return '<h1> The cookie is set with the name : '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)