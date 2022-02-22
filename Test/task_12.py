from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hi():
    return '那个i噢色'


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
        select 商户业务包, sum(差评数), sum(好评数) from distribution_platform
         group by 商户业务包
         order by sum(评价数) desc
    """

    cur.execute(sql)
    res = cur.fetchall()
    for i in res:
        # print(i)
        print('==商户业务包：{}，非好评数：{:.0f}条，好评数：{:.0f}条==='.format(i[0], i[1], i[2]))
    cur.close()
    db.close()
    # return '个别你'
    return render_template('task_12.html', res=res)

if __name__ == '__main__':
    app.run(debug=True)
