from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    items = []
    subtotal = tax = discount = total = 0
    if request.method == "POST":
        items = request.form.getlist("item")
        prices = request.form.getlist("price")
        qtys = request.form.getlist("qty")
        for i in range(len(items)):
            subtotal += float(prices[i]) * int(qtys[i])
        tax = subtotal * 0.05
        if subtotal > 500:
            discount = subtotal * 0.1
        total = subtotal + tax - discount
    return render_template("index.html", subtotal=subtotal, tax=tax,
                           discount=discount, total=total)

