from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app = Flask('app')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST" and "SignupUser" in request.form and "SignupPassword" in request.form:
        pswrd = request.form.get('SignupPassword')
        usrnm = request.form.get('SignupUser')
        con = sqlite3.connect('accounts.db')
        cur = con.cursor()
        accountinfo = [pswrd,usrnm,pswrd]
        cur.execute('insert into account values(?,?,?)', accountinfo)
        con.commit()
        con.close()
        return render_template('index.html')
    return render_template('signup.html')

@app.route("/login", methods = ['post', 'get'])
def login():
    if request.method == "POST" and "loginUser" in request.form and "loginPassword" in request.form:
        input_name = request.form.get('loginUser')
        input_pass = request.form.get('loginPassword')
        con = sqlite3.connect('accounts.db')
        cur = con.cursor()
        cur.execute("select * from account")
        all = cur.fetchall()
        con.commit()
        con.close()
        if input_name and input_pass in all:
            return redirect('main')
        else:
            return redirect('signup')
    return render_template('login.html')
@app.route("/main", methods = ['POST', 'GET'])
def Submit():
    return render_template('main.html')

app.run(port=5000, debug = True)
