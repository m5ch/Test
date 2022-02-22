from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hi():
    return '姑娘十九日'


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
    sql_1 = """
        select count(营业时长) from distribution_platform
        where 营业时长 < 4
    """
    cur.execute(sql_1)
    res_1 = cur.fetchone()
    print('==区间“4小时以内”，商家{}个==='.format(res_1[0]))
    # ******************************************
    sql_2 = """
        select count(营业时长) from distribution_platform
        where 营业时长 between 4 and 6
    """
    cur.execute(sql_2)
    res_2 = cur.fetchone()
    print('==区间“4~6小时”，商家{}个==='.format(res_2[0]))
    # *******************************************
    sql_3 = """
        select count(营业时长) from distribution_platform
        where 营业时长 between 6 and 8
    """
    cur.execute(sql_3)
    res_3 = cur.fetchone()
    print('==区间“6~8小时”，商家{}个==='.format(res_3[0]))
    # *******************************************
    sql_4 = """
        select count(营业时长) from distribution_platform
        where 营业时长 between 8 and 12
    """
    cur.execute(sql_4)
    res_4 = cur.fetchone()
    print('==区间“8~12小时”，商家{}个==='.format(res_4[0]))
    # *********************************************
    sql_5 = """
        select count(营业时长) from distribution_platform
        where 营业时长 > 12
    """
    cur.execute(sql_5)
    res_5 = cur.fetchone()
    print('==区间“12小时以上”，商家{}个==='.format(res_5[0]))


    # data = []
    # for i in range(5):
    #     data.append(list(res_[i][0]))
    # print(data)

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
    cur.close()
    db.close()
    print(data)
    # return "vn艾尔肯读入"
    return render_template('task_10.html', res_1=res_1, res_2=res_2, res_3=res_3, res_4=res_4, res_5=res_5, data=data)


if __name__ == '__main__':
    app.run(debug=True)
