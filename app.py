from flask import Flask, render_template, request, redirect, url_for
import db  # Import the functions from db.py

app = Flask(__name__)

# Home route to display tasks
@app.route('/')
def index():
    tasks = db.get_tasks()  # Fetch tasks from database
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    db.add_task(task)  # Add task to database
    return redirect(url_for('index'))  # Redirect to home page

# Route to mark task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    db.update_task_status(task_id, True)  # Mark task as completed
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    db.delete_task(task_id)  # Delete task from database
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_table()  # Ensure the tasks table is created when the app runs
    app.run(debug=True)
