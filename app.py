import csv
import os
from flask import Flask,render_template, request
from flask import redirect,url_for
app = Flask(__name__, static_url_path='/static')

def create_csv(filename='users.csv'):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password'])
        print(f"CSV file '{filename}' created successfully.")
    else:
        print(f"CSV file '{filename}' already exists.")

# Call create_csv() before using the check_duplicate function
create_csv()

def check_duplicate(username, filename='users.csv'):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False

def add_user(username, password, filename='users.csv'):
    if not check_duplicate(username):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print(f"User {username} added")
        return True
    else:
        print(f"User {username} already exists")
        return False
@app.route('/')
def home():
    return render_template('example.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if add_user(username, password):
        registration_message = "Registration successful!"
        return redirect(url_for('second'))  # Redirect to 'second' endpoint

    else:
        registration_message = "Username already exists."
    return render_template('example.html', registration_message=registration_message)
@app.route('/second')
def second():
    return render_template('secondpage.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return "Login successful!"
    return "Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True)