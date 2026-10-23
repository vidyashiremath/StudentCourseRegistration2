
from flask import Flask, render_template, request, redirect, url_for

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


@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            message = "Please enter both name and email."
        elif any(s["email"].lower() == email.lower()
                 for s in students):
            message = "This email is already registered."
        else:
            students.append({
                "id": len(students) + 1,
                "name": name,
                "email": email
            })
            return redirect(url_for("register"))

    return render_template(
        "register.html",
        students=students,
        message=message
    )


@app.route("/enroll", methods=["GET", "POST"])
def enroll():
    message = ""

    if request.method == "POST":
        student_id = request.form.get("student_id", type=int)
        course_id = request.form.get("course_id", type=int)

        student = next(
            (s for s in students if s["id"] == student_id), None
        )
        course = next(
            (c for c in courses if c["id"] == course_id), None
        )

        if student is None or course is None:
            message = "Please select a valid student and course."
        elif any(
            e["student_id"] == student_id
            and e["course_id"] == course_id
            for e in enrollments
        ):
            message = "This student is already enrolled in this course."
        else:
            enrollments.append({
                "student_id": student_id,
                "course_id": course_id,
                "student_name": student["name"],
                "course_name": course["name"]
            })
            return redirect(url_for("enroll"))

    return render_template(
        "courses.html",
        students=students,
        courses=courses,
        enrollments=enrollments,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
