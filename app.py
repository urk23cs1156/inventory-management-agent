from flask import Flask, render_template, request, redirect
import sqlite3
from agent.restock_agent import restock_decision

app = Flask(__name__)
DB_PATH = "database/inventory.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    items = conn.execute("SELECT * FROM inventory").fetchall()
    conn.close()
    return render_template("index.html", items=items)

@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        threshold = int(request.form["threshold"])

        conn = get_db()
        conn.execute(
            "INSERT INTO inventory (item_name, quantity, min_threshold) VALUES (?, ?, ?)",
            (name, quantity, threshold)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add_item.html")

@app.route("/restock")
def restock():
    conn = get_db()
    items = conn.execute("SELECT * FROM inventory").fetchall()
    conn.close()

    recommendations = []
    for item in items:
        suggestion = restock_decision(item["quantity"], item["min_threshold"])
        if suggestion > 0:
            recommendations.append({
                "name": item["item_name"],
                "current": item["quantity"],
                "threshold": item["min_threshold"],
                "suggested": suggestion
            })

    return render_template("restock.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
