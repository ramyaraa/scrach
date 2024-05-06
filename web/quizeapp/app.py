from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS  # Make sure CORS is handled if you haven't already set this up
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS  # Make sure CORS is handled if you haven't already set this up

app = Flask(__name__)
CORS(app)

users = {}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user_hash = users.get(username)
    if user_hash and check_password_hash(user_hash, password):
        return jsonify({"message": "Login successful", "success": True})
    return jsonify({"message": "Invalid username or password", "success": False}), 401

@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users:
        return jsonify({"message": "Username already exists", "success": False}), 409
    users[username] = generate_password_hash(password)
    return jsonify({"message": "Signup successful. Please log in.", "success": False}), 201

if __name__ == '__main__':
    app.run(debug=True)

