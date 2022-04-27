from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

# 개발하는거 웹페이지에 바로바로 반영되도록 ( 배포할때는 debug=True 없애주기 )
app.run(port=5001, debug=True)