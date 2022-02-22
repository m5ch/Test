from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "训练"
}

db = pymysql.connect(**config)

@app.route('/index')
def index():
    cur = db.cursor()
    sql_1 = """
        select 标品属性, count(标品属性) from distribution_operation
        where 标品属性 like "众包%"
    """
    cur.execute(sql_1)
    res_1 = cur.fetchall()
    print(res_1)

    sql_2 = """
        select 标品属性, count(标品属性) from distribution_operation
        where 标品属性 like "专送%"
    """
    cur.execute(sql_2)
    res_2 = cur.fetchall()
    print(res_2)

    sql_3 = """
        select 标品属性, count(标品属性) from distribution_operation
        where 标品属性 = "自营销"
    """
    cur.execute(sql_3)
    res_3 = cur.fetchall()
    print(res_3[0][1])

    cur.close()
    db.close()
    return render_template('任务三.html', res_1=res_1, res_2=res_2, res_3=res_3)
    # return '是你噶系'



if __name__ == '__main__':
    app.run(debug=True)