import sqlite3
import os

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

INSTANCE_FOLDER = os.path.join(BASE_DIR, "instance")
DB_PATH = os.path.join(INSTANCE_FOLDER, "database.db")

# Create instance folder if it doesn't exist
os.makedirs(INSTANCE_FOLDER, exist_ok=True)

print("Creating DB at:", DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# =========================
# USERS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    profile_image TEXT DEFAULT 'default.png',
    role TEXT DEFAULT 'student',
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# =========================
# COURSES TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    category TEXT NOT NULL,
    duration TEXT NOT NULL,
    description TEXT NOT NULL,
    image TEXT
)
""")

# =========================
# ENROLLMENTS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    progress_percentage INTEGER DEFAULT 0,
    status TEXT DEFAULT 'In Progress',
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id),
    UNIQUE(user_id, course_id)
)
""")

conn.commit()
conn.close()

print("Database created successfully!")