
from flask import Flask, url_for
from flask import render_template,request,redirect,session,url_for
from dbms import adddata,show_data
import pymysql as p
app = Flask(__name__)


app.secret_key ="a123b23c45"
def getconnection():
    return p.connect(host="localhost",user="root",password="",database="spicyfood")

'''Home page calling fun'''
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/savelink', methods=['POST'])
def save():
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    phone = request.form["phone"]
    zip = request.form["zip"]
    city = request.form["city"]
    state= request.form["state"]
    address = request.form["address"]
    user = request.form["username"]
    pass1 = request.form["password"]
    #tuple add in databases
    t = (fname, lname, email,phone,zip,city,state,address,user,pass1)
    adddata(t)
    return render_template('register.html')



@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/adminfun', methods=["POST"])
def adminfun():
    username = "admin"
    passwd = "admin@123"
    if request.method==['post'] and request.form["admin"] == username and request.form["pass"] == passwd:
        return render_template('admin.html')
        
    else:
        
        return showfun()

@app.route("/showlink")
def showfun():
    datalist=show_data()
    return render_template("data.html",data=datalist)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginfun',methods=["GET","POST"])
def loginfun():
    msg =" "
    if request.method=="post" and 'username' in request.form and 'password' in request.form:
        username = request.form["username"]
        password = request.form["password"]
        con= getconnection()
        cur = con.cursor()
        cur.execute('Select * from Registration where USERNAME= %s and PASS= %s'.format(username,password))
        account = cur.fetchone()
        if account:
            session['k'] = True
            msg = 'Login Successfully !!'
            return render_template('store.html',msg=msg)
        else:
            msg="incorrect username / password"
            
    return render_template('store.html', msg = msg)

@app.route('/logout')
def logout():
    return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0", port=80, debug=True)




