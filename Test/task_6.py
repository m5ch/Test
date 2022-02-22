from flask import Flask
import pymysql

app = Flask(__name__)


@app.route('/')
def hi():
    return '法国尿素'


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
        select city_name, count(city_name) from store_basic_informations
        group by city_name
        order by count(city_name) desc
    """
    cur.execute(sql)
    res = cur.fetchall()
    for i in range(len(res)):
        print('=={}.城市:{},商家{}个==='.format(i, res[i][0], res[i][1]))
    cur.close()
    db.close()
    return "你该睡觉"


if __name__ == '__main__':
    app.run(debug=True)
