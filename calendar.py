from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Seznam událostí – každá událost má datum, popis a stav splnění
events = []

@app.route("/")
def index():
    print("Preparing...")
    return render_template("index.html", events=events)

@app.route("/add", methods=["POST"])
def add_event():
    date = request.form["date"]
    description = request.form["description"]
    events.append({"date": date, "description": description, "done": False})
    return redirect("/")

@app.route("/delete/<int:index>", methods=["POST"])
def delete_event(index):
    if 0 <= index < len(events):
        del events[index]
    return redirect("/")

@app.route("/toggle/<int:index>", methods=["POST"])
def toggle_event(index):
    if 0 <= index < len(events):
        events[index]["done"] = not events[index]["done"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

