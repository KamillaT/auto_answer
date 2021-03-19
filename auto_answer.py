from flask import Flask, request, url_for, render_template
import json

app = Flask(__name__)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    with open("answer.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('auto_answer.html', news=news_list)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
