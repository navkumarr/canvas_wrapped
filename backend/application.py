from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from user import User
import os

app = Flask(__name__, static_folder='frontend/build', static_url_path='/') 
CORS(app)

@app.route('/api/assignments', methods=['GET'])
def get_assignments():
    user1 = User()
    user1.assignments.sort(key=lambda x: x['due_date'])

    formatted_assignments = [
        {
            "course": assignment['course'],
            "assignment": assignment['assignment'],
            "due_in_days": (assignment['due_date'] - user1.now).days
        }
        for assignment in user1.assignments
    ]
    return jsonify(formatted_assignments)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)