# Canvas Wrapped

## Overview

This project is a (proof of concept) web application for tracking assignments from a Canvas LMS account. The backend is built using Flask, and the frontend is created with React. The application retrieves assignment data from Canvas and displays upcoming assignments sorted by their due dates. In the future, the goal is to organize these assignments and provide users with automations they can pick from, guaranteeing they don't forget to submit assignments on time.

## Features

- Fetch assignments from the Canvas LMS API.
- Display assignments for the next 7 days.
- React-based frontend served by Flask.

## Technologies Used

- **Backend**: Flask, Python, Gunicorn
- **Frontend**: React.js
- **Canvas API**: For fetching user assignments
- **Deployment**: Heroku

---

## Project Structure

```
project/
├── application.py        # Flask app configuration
├── user.py               # Logic for interacting with Canvas API
├── frontend/             # React frontend source
│   ├── src/              # React source files
│   ├── build/            # Production-ready static files
├── requirements.txt      # Python dependencies
├── Procfile              # Heroku process file
├── runtime.txt           # Python runtime for Heroku
```

---

## Installation

### Prerequisites

- Python 3.7+
- Node.js (for building the frontend)

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-name.git
   cd project
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add environment variables for Canvas API:

   - `API_URL`: Your Canvas instance URL
   - `API_KEY`: Your Canvas API key

5. Run the Flask app locally:

   ```bash
   python application.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:

   ```bash
   npm install
   ```

3. Build the React frontend:

   ```bash
   npm run build
   ```

   The `build/` folder will be created and used by Flask to serve static files.

---

## Deployment (Heroku)

### Steps

1. Ensure all changes are committed:

   ```bash
   git add .
   git commit -m "Prepare for deployment"
   ```

2. Log in to Heroku:

   ```bash
   heroku login
   ```

3. Create a new Heroku app:

   ```bash
   heroku create
   ```

4. Add the Heroku Git remote:

   ```bash
   heroku git:remote -a your-heroku-app-name
   ```

5. Deploy the app:

   ```bash
   git push heroku main
   ```

6. Open the deployed app:

   ```bash
   heroku open
   ```

---

## Usage

1. Navigate to the deployed app's URL.
2. The app will display assignments due within the next 7 days, sorted by due date.

---

## Notes

- Ensure your Canvas API key has sufficient permissions to access assignments.
- Update environment variables on Heroku using:
  ```bash
  heroku config:set API_URL="your_canvas_url" API_KEY="your_canvas_api_key"
  ```

---

# Future Improvements

- Deploy to web (undiagnosed issue with Heroku)
- Add ability to handle new users through Firebase
- Add planned features
- Improve error handling for API failures.
- Enhance frontend UI/UX.

---

## License

This project is licensed under the MIT License.

