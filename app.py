from flask import Flask , render_template
from data import Articles
#render_template html과 만나면 해당 템플릿으로 변환시켜 줌.
app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET']) #데커레이터  경로 라우팅, 방식(지금은 리스트)
def index():
    # return "Hello World"
    return render_template("index.html", data= "DONG")
    # 첫번째 인자 html경로, 두번째는 전달할 데이터
@app.route('/about')
def about():
    return render_template("about.html", hello = "Gary Kim")

@app.route('/articles')
def articles():
    articles = Articles()
    print(articles[0]['title'])
    return render_template("articles.html", articles = articles)

@app.route('/article/<int:id>')
def article(id):
    articles = Articles()
    article = articles[id-1]
    print(articles[id-1])
    return render_template("article.html", article = article)

if __name__ == '__main__': ##처음 서버 띄우는 곳, 초기 실행
    app.run()