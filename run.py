from flask import Flask,request,render_template
import datetime
app = Flask(__name__)

@app.route('/path')
def path():
    return  str(datetime.datetime.now())
@app.route('/')
def hello():
    return 'Hello World'

app.run(host='0.0.0.0',
        port=8080,
        debug=True)


















































