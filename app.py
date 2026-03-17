from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

students = []

@app.route('/')
def home():
    html = """
    <html>
    <head>
        <title>Student Registration</title>
        <style>
            body{
                background: skyblue;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container{
                background: white;
                padding: 30px;
                border-radius: 10px;
                width: 350px;
                box-shadow: 0px 0px 10px gray;
                text-align: center;
            }

            h1{
                color: #333;
            }

            input{
                width: 90%;
                padding: 8px;
                margin: 8px 0;
            }

            button{
                background: skyblue;
                border: none;
                padding: 10px;
                width: 100%;
                color: white;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover{
                background: deepskyblue;
            }

            ul{
                text-align: left;
            }
        </style>
    </head>

    <body>

    <div class="container">
        <h1>Student Registration</h1>

        <form action="/add" method="post">
            <input type="text" name="name" placeholder="Student Name" required><br>
            <input type="number" name="grade" placeholder="Grade" required><br>
            <input type="text" name="section" placeholder="Section" required><br>
            <button type="submit">Register</button>
        </form>

        <h3>Student List</h3>
        <ul>
        {% for s in students %}
            <li>{{s.name}} - Grade {{s.grade}} ({{s.section}})
            <a href="/delete/{{s.id}}">Delete</a></li>
        {% endfor %}
        </ul>
    </div>

    </body>
    </html>
    """
    return render_template_string(html, students=students)


@app.route('/add', methods=['POST'])
def add_student():
    new_id = len(students) + 1
    students.append({
        "id": new_id,
        "name": request.form["name"],
        "grade": request.form["grade"],
        "section": request.form["section"]
    })
    return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
