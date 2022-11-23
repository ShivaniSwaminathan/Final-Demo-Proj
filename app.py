from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def home():  
    return render_template("home.html");  
 
@app.route("/about")  
def about():  
    return render_template("about.html");  
@app.route("/package")  
def package():  
    return render_template("package.html"); 
@app.route("/book")  
def book():  
    return render_template("book.html"); 
@app.route("/cruise tour")  
def cruise():  
    return render_template("cruise tour.html");
@app.route("/Family tour")  
def family():  
    return render_template("Family tour.html");  
@app.route("/himachal")  
def himachal():  
    return render_template("himachal delight.html");
@app.route("/weekend")  
def weekend():  
    return render_template("weekend.html");

@app.route("/Religious")  
def Religious():  
    return render_template("Religious tour.html");

@app.route("/ocenia")  
def ocenia():  
    return render_template("ocenia.html");

@app.route("/Singapore")  
def Singapore():  
    return render_template("Singapore.html");


@app.route("/Srilanka")  
def Srilanka():  
    return render_template("Srilanka.html");

@app.route("/UAE")  
def UAE():  
    return render_template("UAE.html");

@app.route("/Tamilnadu")  
def Tamilnadu():  
    return render_template("Tamilnadu.html");

@app.route("/Bali")  
def Bali():  
    return render_template("Bali.html");

@app.route("/login")  
def login():  
    return render_template("login.html");  
@app.route("/signup")  
def signup():  
    return render_template("signup.html");  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            passw = request.form["pas"]  
            email=request.form['email']
            with sqlite3.connect("Customers.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Customers (cname,email,Password) values (?,?,?)",(name,email,passw))  
                con.commit()  
                msg = "SignedUp Successfully!"  
        except:  
            con.rollback()  
            msg = "We can not add the Customer to the list"  
        finally:  
            return render_template("login.html",msg = msg)  
            con.close()  
 
@app.route("/validatedetails",methods = ["POST","GET"])
def validate():
    msg = "login failed"  
    if request.method == "POST":    
            name = request.form["name"]  
            passw = request.form["pas"] 
            with sqlite3.connect("Customers.db") as con:  
                cur = con.cursor() 
                statement = f"SELECT cname from Customers WHERE cname='{name}' AND Password = '{passw}'"
                cur.execute(statement)  
                if  not cur.fetchone():  
                    return render_template("loginfailed.html",msg = msg)
                else:
                    return  render_template("home.html")


  
if __name__ == "__main__":  
    app.run(debug = True,port=3000)  