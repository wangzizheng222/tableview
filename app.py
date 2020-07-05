import pymysql
import yagmail
from flask import Flask, render_template, json


def read_data(table_name):
    # 打开数据库连接
    print("开始连接")
    db = pymysql.connect("139.196.168.156", "my_data", "2804355025", "my_data")
    # db = pymysql.connect("localhost", "root", "2804355025", "qingxie")
    print("成功连接")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select * from " + table_name + " order by 时长 desc "
    # sql = "select * from data order by 时长 desc "
    cursor.execute(sql)
    rs = cursor.fetchall()

    # 关闭数据库连接
    db.close()
    print("关闭连接")
    return rs


app = Flask(__name__)


@app.route("/table")
def table_list():
    return render_template("table_list.html")


@app.route("/table/<table_name>")
def table_view(table_name):
    data = read_data(table_name)
    return render_template("Table.html", res=json.dumps(data))


@app.route("/callback")
def callback():
    return render_template("Callback.html")


@app.route("/callback/submit_callback/<email_data>", methods=["POST", "GET"])
def submit_callback(email_data):
    try:
        yag = yagmail.SMTP(user="2804355025@qq.com", password="txklejrstsiadgeg", host="smtp.qq.com", )
        yag.send("2804355025@qq.com", subject="网站反馈", contents=email_data)
        return render_template("email_send_successfully.html")
    except:
        return render_template("email_send_failed.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/welcome")
def welcome():
    return render_template("Welcome.html")


@app.route("/callback_new")
def callback_new():
    return render_template("Callback_new.html")


@app.route("/management")
def management():
    return render_template("Management.html")


if __name__ == '__main__':
    app.run(port=8080)

