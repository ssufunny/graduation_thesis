from flask import Flask
import random
app = Flask(__name__)

[{'id':1, 'title': html}]
#기본페이지
@app.route('/')
def index():
    return '''<!doctype html>
    <html>
        <body>
            <h1><a = href="/">WEB</a></h1>
            <ol>

@app.route('/create/')
def create():
    return 'Create'

# 개발하는거 웹페이지에 바로바로 반영되도록 ( 배포할때는 debug=True 없애주기 )
app.run(port=5001, debug=True)