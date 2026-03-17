from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

# simple storage
students = [
    {"id": 1, "name": "John", "grade": 10, "section": "Zechariah"}
]

# HOMEPAGE
@app.route('/')
def home():
    html = """
    <h1>Student Management</h1>

    <h2>Add Student</h2>
    <form action="/add" method="post">
        Name: <input type="text" name="name"><br>
        Grade: <input type="number" name="grade"><br>
        Section: <input type="text" name="section"><br>
        <button type="submit">Add Student</button>
    </form>

    <h2>Student List</h2>
    <ul>
    {% for student in students %}
        <li>
            {{student.name}} - Grade {{student.grade}} ({{student.section}})
            <a href="/delete/{{student.id}}">Delete</a>
        </li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, students=students)


# CREATE STUDENT
@app.route('/add', methods=['POST'])
def add_student():
    new_id = len(students) + 1
    name = request.form['name']
    grade = request.form['grade']
    section = request.form['section']

    students.append({
        "id": new_id,
        "name": name,
        "grade": grade,
        "section": section
    })

    return redirect(url_for('home'))


# DELETE STUDENT
@app.route('/delete/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return redirect(url_for('home'))


# EDIT STUDENT
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((s for s in students if s["id"] == id), None)

    if request.method == "POST":
        student["name"] = request.form["name"]
        student["grade"] = request.form["grade"]
        student["section"] = request.form["section"]
        return redirect(url_for('home'))

    html = """
    <h1>Edit Student</h1>
    <form method="post">
        Name: <input type="text" name="name" value="{{student.name}}"><br>
        Grade: <input type="number" name="grade" value="{{student.grade}}"><br>
        Section: <input type="text" name="section" value="{{student.section}}"><br>
        <button type="submit">Update</button>
    </form>
    """
    return render_template_string(html, student=student)


if __name__ == "__main__":
    app.run(debug=True)
