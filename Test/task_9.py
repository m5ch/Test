from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hi():
    return "感觉农户色弱姑获鸟"


config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "训练",
}


@app.route('/index')
def index():
    db = pymysql.connect(**config)
    cur = db.cursor()
    sql = """
        
    """
    cur.close()
    db.close()
    return '给你哦按实际入库'


if __name__ == '__main__':
    app.run(debug=True)
