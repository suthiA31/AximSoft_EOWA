# HireVerse - Flask Job Portal

HireVerse is a full-stack Job Portal web application built using Flask. It allows employers to post jobs and manage applicants, while candidates can search for jobs, apply with resumes, and manage their profiles.

---

## Features

### Authentication
- User Registration
- Email OTP Verification
- Secure Login
- Login OTP Verification
- Password Hashing using Werkzeug
- Logout

### Candidate
- View Latest Jobs
- Search Jobs
- Filter Jobs by Category
- Apply for Jobs
- Upload Resume (PDF)
- Save Jobs
- Edit Profile
- Upload Profile Picture
- Resume Skill Matching
- View Application Status

### Employer
- Employer Dashboard
- Post New Jobs
- Edit Jobs
- Delete Jobs
- View Applicants
- Open Resume inside Website
- Schedule Interviews
- View Notifications
- Employer Profile

### Email Notifications
- Registration OTP
- Login OTP
- Welcome Email
- Login Alert
- Interview Scheduling Email

### Resume Parser
- Extract text from PDF Resume
- Detect Candidate Skills
- Calculate Resume Match Score

---

## Technologies Used

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Mail
- Flask-Migrate
- Flask-WTF

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

### Database
- SQLite

### Libraries
- pdfplumber
- Werkzeug
- python-dotenv

---

## Project Structure

```
CareerHub/
│
├── auth/
├── candidate/
├── employer/
├── jobs/
├── templates/
├── static/
├── utils/
├── migrations/
├── instance/
│
├── app.py
├── models.py
├── config.py
├── extension.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/suthiA31/AximSoft_EOWA.git
```

```bash
cd AximSoft_EOWA
```

### Create Virtual Environment

Linux

```bash
python3 -m venv .venv
```

Activate

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

MAIL_USERNAME=your_email@gmail.com

MAIL_PASSWORD=your_app_password
```

---

## Database Migration

```bash
flask db init
```

```bash
flask db migrate -m "Initial Migration"
```

```bash
flask db upgrade
```

---

## Run Application

```bash
python app.py
```

Application runs at

```
http://127.0.0.1:5000
```

---

## Modules

### Authentication
- Register
- Login
- OTP Verification
- Email Notifications

### Candidate
- Dashboard
- Profile
- Resume Upload
- Saved Jobs
- Applications

### Employer
- Dashboard
- Job Management
- Applicants
- Resume Viewer
- Interview Scheduler

### Jobs
- Browse Jobs
- Search Jobs
- Job Details
- Categories

---

## Resume Matching

The application extracts skills from uploaded PDF resumes using **pdfplumber**.

Supported skills include:

- Python
- Flask
- Django
- SQL
- MySQL
- MongoDB
- Java
- HTML
- CSS
- JavaScript
- Bootstrap

A match score is calculated between candidate skills and job requirements.

---

## Future Enhancements

- Admin Panel
- Company Verification
- AI Resume Recommendation
- AI Interview Questions
- Job Recommendation System
- Chat Between Employer and Candidate
- Password Reset via Email
- Pagination
- Advanced Filters

---

## Developer

**Suthishna Kumar**

Flask Full Stack Development Project

---

## License

This project is developed for educational and learning purposes.
