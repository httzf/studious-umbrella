from flask import Flask, render_template, url_for, request, redirect, flash, session

users = [
    {'username': 'httzf', 'password': "123321"}
]


app = Flask(__name__)
app.secret_key = 'SECRET'


@app.route('/') # endpoint, по умолчанию заходит под /
def hello():    # функция представления
     return f"""
    <p>сайт начиающего верстальщика. Есть ссылки: </p>
        <a href={url_for('index')}>Site</a>
        <a href={url_for('start')}>стартовая страница</a>
        <a href={url_for('base')}>базовая страница</a>
        <a href={url_for('form')}>форма для вопросов</a>
        <a href={url_for('login')}>форма для регистрации</a>
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


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        for item in request.form:
            print(request.form[item])
    return render_template('form.html') # отрисовывает шаблон


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if session.get('username'):
            return render_template('login.html')
        for user in users:
            if request.form['login'] == user['username']:
                if request.form['password'] == user['password']:
                   flash('Зарегался', 'success')
                   session['username'] = user['username']
                   return redirect(url_for('profile', username=user['username']))
                else:
                    flash('Wrong password', 'error')
            else:
                if session.get('username'):
                    return redirect(url_for('profile', username=session['username']))
            return render_template('login.html')


@app.route('/profile/<username>')
def profile(username):
    if username == session.get('username'):
        return render_template('login.html', username=username)
    flash('Доступ запрещен', 'error')
    return redirect(url_for('login', username=session['username']))


if __name__ == '__main__':
    app.run(debug=True)











