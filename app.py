from flask import Flask, request, render_template
import pyodbc
import logging

app = Flask(__name__)

# Define the connection string
conn_str = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:database-form.database.windows.net,1433;Database=database-form;Uid=moraesl95;Pwd={3tikD7f8o9!};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    # Get the form data
    name = request.form.get('name')
    email = request.form.get('email')

    try:
        # Connect to the database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Insert the user data into the database
        cursor.execute("INSERT INTO users (name, email) VALUES (?,?)", (name, email))
        conn.commit()

        return 'User added successfully'
    except Exception as e:
        logging.error("Error in adding user: %s", str(e))
        return 'Error in adding user: {}'.format(str(e))

if __name__ == '__main__':
    app.run(debug=True)
