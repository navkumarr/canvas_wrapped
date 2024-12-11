from flask import Flask, jsonify
from flask_cors import CORS
from user import User

app = Flask(__name__)
CORS(app)  # Allow requests from different origins (e.g., React frontend)

@app.route('/api/assignments', methods=['GET'])
def get_assignments():
    user1 = User()
    user1.assignments.sort(key=lambda x: x['due_date'])

    # Format assignments into JSON-friendly data
    formatted_assignments = [
        {
            "course": assignment['course'],
            "assignment": assignment['assignment'],
            "due_in_days": (assignment['due_date'] - user1.now).days
        }
        for assignment in user1.assignments
    ]
    
    return jsonify(formatted_assignments)

if __name__ == '__main__':
    app.run(debug=True)
