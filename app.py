from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")

    return f"""
    <h2>Form Submitted Successfully</h2>
    <p>Name: {name}</p>
    <p>Email: {email}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
