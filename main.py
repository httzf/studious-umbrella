from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/') # endpoint, по умолчанию заходит под /
def hello():    # функция представления
     return f"""
    <a href={url_for('index')}>Site</a>
    <a href={url_for('start')}>стартовая страница</a>
    <a href={url_for('base')}>базовая страница</a>
"""

@app.route('/start')
def start():
    return render_template('start.html') # отрисовывает шаблон

@app.route('/base')
def base():
    return render_template('base.html') # отрисовывает шаблон


@app.route('/index')
def index():
    return render_template('index.html') # отрисовывает шаблон

@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html') # отрисовывает шаблон

@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html') # отрисовывает шаблон


if __name__ == '__main__':
    app.run(debug=True)











