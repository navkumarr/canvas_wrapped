import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Assignments = () => {
  const [assignments, setAssignments] = useState([]);

  useEffect(() => {
    // Fetch data from the Python backend
    axios.get('http://localhost:5000/api/assignments')
      .then(response => {
        setAssignments(response.data);
      })
      .catch(error => {
        console.error('Error fetching assignments:', error);
      });
  }, []);

  return (
    <div>
      <h1>Upcoming Assignments</h1>
      {assignments.length > 0 ? (
        <ul>
          {assignments.map((assignment, index) => (
            <li key={index}>
              <strong>{assignment.course}</strong>: {assignment.assignment} (Due in {assignment.due_in_days} days)
            </li>
          ))}
        </ul>
      ) : (
        <p>No assignments due this week!</p>
      )}
    </div>
  );
};

export default Assignments;
