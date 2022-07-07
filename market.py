from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", name="Joseph gakumo")


@app.route("/about")
def about():
    items=["id:1", "name:Iphone", "SerialNumber:312rrsaw2", "price:12000",
           "id:2", "name:Desktop", "SerialNumber:312rr1w22", "price:25000",
           "id:3", "name:Laptop", "SerialNumber:312rrsrw2", "price:30000", 
           "id:4", "name:Macbook", "SerialNumber:312rrsaw5", "price:50000",]
    return render_template("about.html", items=items)