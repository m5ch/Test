from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/index')
def home():
    return render_template('home.html')


@app.route('/')
def index_1():
    # return render_template('home.html')
    return home()


@app.route('/home')
def index_2():
    # return render_template('home.html')
    return home()


@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect('movie.db')
    cur = con.cursor()
    sql = "select * from movie250"
    data = con.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('movie.html', movies = datalist)


@app.route('/score')
def score():
    return render_template('score.html')


@app.route('/wordcloud')
def wordcloud():
    return render_template('/wordcloud.html')


@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
