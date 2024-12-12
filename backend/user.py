from canvasapi import Canvas
from canvasapi.exceptions import CanvasException
import datetime

API_URL = "https://canvas.wisc.edu"
API_KEY = "8396~XVZFcCKxzFUY4XLA3zCfTJhRcY8VrfR4EPA8AB33wK3ukPYa7QKYCuLXeQe3uRYU"

class User:
    def __init__(self):
        # Define the current time and the time one week from now
        self.now = datetime.datetime.utcnow()
        self.one_week = self.now + datetime.timedelta(weeks=1)

        # Initialize the canvas object
        self.canvas = Canvas(API_URL, API_KEY)

        # Get the current user
        self.user = self.canvas.get_current_user()

        # Get user courses
        self.courses = self.user.get_courses(enrollment_state='active')

        # Initialize the list to hold upcoming items
        self.assignments = []

        # Iterate over each course
        for course in self.courses:
            # Get assignments for the course
            course_assignments = course.get_assignments()
            for assignment in course_assignments:
                if assignment.due_at:
                    due_date = datetime.datetime.strptime(assignment.due_at, '%Y-%m-%dT%H:%M:%SZ')
                    if self.now <= due_date <= self.one_week:
                        self.assignments.append({
                            'course': course.name,
                            'assignment': assignment.name,
                            'due_date': due_date
                        })