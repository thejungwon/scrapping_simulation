from flask import request, render_template, flash, redirect, url_for
from flask import Flask


 
app = Flask(__name__)

 
@app.route('/', methods=['GET'])
def index():
      # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
      return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    
    host = request.headers.get("Host")
    referer = request.headers.get("Referer")
    
    user_agent = request.headers.get('User-Agent')
    
    

    if 'python' in  request.headers.get('User-Agent'):
        return '너 크롤링 하는거지!?'

    if not referer or host not in referer:
        return '나는 내 웹사이트에서만 호출 가능하지롱~!'

    return '나는 안보일거야 ㅋㅋ, 가져갈 수 있으면 가져가봐!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)