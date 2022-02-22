from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hi():
    return '那个i打赏'


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
        select 商户业务包, count(商户业务包), sum(用户投诉数) from distribution_platform
        group by 商户业务包
        order by sum(用户投诉数) desc
    """
    cur.execute(sql)
    res = cur.fetchall()
    # for i in res:
    #     print(i)
    # for i in range(len(res)):
    #     print('商户业务包：{},商家数量：{}家，投诉{:.0f}条记录'.format(res[i][0], res[i][1], res[i][2]))
    # print('1.商户业务包：大客户,  商家数量：{}家，投诉{:.0f}条记录'.format(res[0][1], res[0][2]))
    # print('2.商户业务包：家庭,  商家数量：{}家，投诉{:.0f}条记录'.format(res[1][1], res[1][2]))
    # print('3.商户业务包：其他,  商家数量：{}家，投诉{:.0f}条记录'.format(res[2][1], res[2][2]))
    # print('4.商户业务包：小客户,  商家数量：{}家，投诉{:.0f}条记录'.format(res[3][1], res[3][2]))
    # print('5.商户业务包：高校,  商家数量：{}家，投诉{:.0f}条记录'.format(res[4][1], res[4][2]))
    # print('6.商户业务包：白领,  商家数量：{}家，投诉{:.0f}条记录'.format(res[5][1], res[5][2]))
    cur.close()
    db.close()
    # return '工农上帝'
    return render_template('task_11.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)
