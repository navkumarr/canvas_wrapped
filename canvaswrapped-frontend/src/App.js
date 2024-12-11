import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Assignments.css'; // Import CSS for neumorphic design

const Assignments = () => {
  const [assignments, setAssignments] = useState([]);

  useEffect(() => {
    // Fetch data from the Python backend
    axios.get('http://localhost:5000/api/assignments')
      .then(response => {
        // Sort by class and due date
        const sortedData = response.data.sort((a, b) => {
          if (a.course < b.course) return -1;
          if (a.course > b.course) return 1;
          return new Date(a.due_date) - new Date(b.due_date);
        });
        setAssignments(sortedData);
      })
      .catch(error => {
        console.error('Error fetching assignments:', error);
      });
  }, []);

  return (
    <div className="assignments-container">
      <h1 className="title">Upcoming Assignments</h1>
      {assignments.length > 0 ? (
        <ul className="assignments-list">
          {assignments.map((assignment, index) => (
            <li className="assignment-item" key={index}>
              <div className="assignment-card">
                <h3 className="course-name">{assignment.course}</h3>
                <p className="assignment-name">{assignment.assignment}</p>
                <p className="due-date">Due in {assignment.due_in_days} days</p>
              </div>
            </li>
          ))}
        </ul>
      ) : (
        <p className="no-assignments">No assignments due this week!</p>
      )}
    </div>
  );
};

export default Assignments;
