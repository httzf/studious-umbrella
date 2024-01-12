from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <a href={url_for('index')}>Site</a>
"""

@app.route('/index')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)











