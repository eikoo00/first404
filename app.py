
from flask import Flask, render_template,request,redirect,session
import sqlite3
app = Flask(__name__)

app.secret_key='shop_tarmie'



@app.route("/yshop1")
def yshop1():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 1")
    shop_info = c.fetchone()
    c.close()

    return render_template('yshop1.html',shop_info=shop_info)

@app.route("/yshop2")
def yshop2():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 2")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop2.html',shop_info=shop_info)

@app.route("/yshop3")
def yshop3():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 3")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop3.html',shop_info=shop_info)

@app.route("/yshop4")
def yshop4():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 4")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop4.html',shop_info=shop_info)

@app.route("/yshop5")
def yshop5():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 5")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop5.html',shop_info=shop_info)

@app.route("/yshop6")
def yshop6():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 6")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop6.html',shop_info=shop_info)


@app.route("/yshop7")
def yshop7():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 7")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop7.html',shop_info=shop_info)

@app.route("/yshop8")
def yshop8():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 8")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop8.html',shop_info=shop_info)

@app.route("/yshop9")
def yshop9():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 9")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop9.html',shop_info=shop_info)

@app.route("/yshop10")
def yshop10():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 10")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop10.html',shop_info=shop_info)

@app.route("/yshop11")
def yshop11():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 11")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop11.html',shop_info=shop_info)

@app.route("/yshop12")
def yshop12():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 12")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop12.html',shop_info=shop_info)

@app.route("/yshop13")
def yshop13():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 13")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop13.html',shop_info=shop_info)

@app.route("/yshop14")
def yshop14():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 14")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop14.html',shop_info=shop_info)

@app.route("/yshop15")
def yshop15():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shop where id = 15")
    shop_info = c.fetchone()
    c.close()
    return render_template('yshop15.html',shop_info=shop_info)



if __name__ == '__main__':
    app.run(debug=True)