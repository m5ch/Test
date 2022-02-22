from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


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
        select second_auditor_id, count(second_auditor_id), sum(status), second_auditor_name from distribution_platform_data
        group by second_auditor_name 
        order by count(status) desc
        limit 10
    """
    cur.execute(sql)
    res = cur.fetchall()
    for i in range(len(res)):
        print('=={}.二级审核人id:{},审批数量:{}条,其中通过{:.0f}条，拒绝{:.0f}条==={}'.format(i + 1, res[i][0], res[i][1], res[i][2],
                                                                           res[i][1] - res[i][2], res[i][3]))
    # print(res)
    cur.close()
    db.close()
    # return "你改哦二哥"
    return render_template('task_7.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)
