from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hi():
    return "hi"


config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "训练"
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
    res = cur.fetchmany(10)
    data = []
    for i in res:
        # print(i)
        data.append(list(i))
    print(data)
    cur.close()
    db.close()
    # return "OK?"
    return render_template('task_4.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
