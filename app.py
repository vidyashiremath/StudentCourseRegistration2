
from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {"id": 1, "name": "Python Programming"},
    {"id": 2, "name": "Web Development"},
    {"id": 3, "name": "Machine Learning"}
]

students = []
enrollments = []


@app.route("/")
def home():
    return render_template("index.html", courses=courses)


if __name__ == "__main__":
    app.run(debug=True)
