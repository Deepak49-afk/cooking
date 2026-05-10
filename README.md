# Cloud Kitchen - Recipe Sharing Platform

Cloud Kitchen is a full-stack, responsive recipe sharing platform. It allows users to discover, save, and share their favorite recipes, as well as interact with others through likes and comments in real-time.

## Tech Stack
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (Vanilla)
- **Backend**: Python, Flask, Flask-SocketIO
- **Database**: MongoDB (PyMongo)
- **Authentication**: JWT, bcrypt

## Setup Instructions

### 1. Backend Setup
1. Open a terminal and navigate to the `backend` directory.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables (optional):
   Create a `.env` file in the `backend` directory and add `MONGO_URI=mongodb://localhost:27017/cooing` if different from default.
5. Run the Flask application:
   ```bash
   python app.py
   ```
   The backend will start at `http://localhost:5000`.

### 2. Frontend Setup
1. The frontend is entirely static HTML/CSS/JS.
2. You can serve it using any simple HTTP server (e.g., Live Server in VSCode).
   ```bash
   # From the frontend directory:
   cd frontend
   npx serve .
   ```
3. Open `http://localhost:3000/login.html` (or whichever port your server uses) in your browser to get started.

## Features implemented
- Premium responsive UI with Glassmorphism
- Full JWT-based user authentication system
- Profile personalization and image uploads
- Advanced recipe search, filtering, and sorting
- Real-time notifications and comment tracking
- Liking and saving recipes
