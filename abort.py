'''
Redirect means directly use go thorgh the another page link '''

from flask import Flask,redirect,render_template,url_for,request,abort
app=Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        if request.form["name"]=="Rahul":
                return redirect(url_for("success"))
        else : abort(403)       # if name is not equal to Rahul , then abort 404 eoor shown
    return '<h1> Please go throuth form "/" url</h>'    # use when get method occurs (ex- runn the machine and instead follow link go to the web and type url - localhost/5000/login )

@app.route("/success")
def success():
    return '<h1> Hello, You are succesfully login</h?'

if __name__=="__main__":
    app.run(debug=True)

'''
Types of falsk abort :
400 : Bad request
401 : Unauthorized
403 : Forbidden
404 : Not found
406 : Not acceptable
415 : Unsupported media type
429 : Too many requests


'''