# To-Do List Web Application (Flask with SQLite)

This is a simple yet professional **To-Do List** web application built using **Flask**, **SQLite**, and modern web design principles. The application allows users to add tasks, mark them as completed, and delete them. It's a perfect starting point for anyone wanting to build a full-stack web application using Python and SQLite.

## Features

- **Add a task**: Users can add new tasks to their to-do list.
- **Mark task as completed**: Users can mark tasks as completed with a single click.
- **Delete a task**: Users can delete any task from their list.
- **Responsive design**: The app is fully responsive and works perfectly on desktop and mobile devices.

## Tech Stack

- **Frontend**: HTML, CSS (with custom modern design)
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Libraries/Tools**:
  - Flask (Python web framework)
  - SQLite (database)
  - Bootstrap (for styling and responsive design)

## Setup Instructions

### Prerequisites

Ensure that you have the following installed on your system:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pip** (Python package installer)

### Steps to Run the Project Locally

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/pandeyayush0811/To-do-Planner.git
    cd To-do-list
    ```

2. **Set up a virtual environment** (recommended):

    - For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - For macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    This will install Flask and other necessary dependencies.

4. **Set up SQLite database**:

    The SQLite database will be automatically created when you run the app for the first time.

5. **Run the Flask app**:

    ```bash
    python app.py
    ```

    The app will be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

6. **Open the app in your browser**:

    Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to start using the To-Do List web app.

## Folder Structure

To-do-list/ │ ├── app.py # Main Flask application file ├── requirements.txt # List of Python dependencies ├── templates/ # HTML templates │ ├── index.html # Main page template ├── static/ # Static files (CSS, JS, images) │ └── style.css # Custom CSS for styling ├── .gitignore # Git ignore file ├── README.md # Project documentation └── database.db # SQLite database file (created on app run)



### Important Files

- `app.py`: Contains the main Flask application, including routes and logic to interact with the SQLite database.
- `requirements.txt`: Contains a list of Python libraries to install (Flask, etc.).
- `templates/`: Folder containing HTML files used by Flask's rendering system.
- `static/`: Contains static files like CSS and JavaScript for the frontend.
- `database.db`: The SQLite database file that stores all the to-do tasks.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. Please ensure that your code adheres to the existing code structure and passes any tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Ayush Pandey** – [GitHub Profile](https://github.com/pandeyayush0811)

## Acknowledgments

- **Flask** – A micro web framework written in Python.
- **SQLite** – A self-contained, serverless, and zero-configuration SQL database engine.
- **Bootstrap** – A front-end framework for building responsive, mobile-first websites.

---

Feel free to modify this template as per your project details! Let me know if you need any additional help. 😊
