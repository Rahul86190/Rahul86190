from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    str='''
<html>
<head>
<title>Home</title>
</head>
<body>
<h1>Home</h1>
<h2>This is the home page.</h2>
<h3>This page is generated by Flask. Without using any template seperate code.</h3>
<h2>This page's Html code is wriiten within function of python.</h2>

</body>
</html>
'''
    return str

if __name__ == '__main__':
    app.run(debug=True)