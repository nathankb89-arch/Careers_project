import os
import sqlite3

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "career_compass.db")


def get_connection():
    """Open a connection to the local SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create tables and load sample data for a new project."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            education TEXT,
            skills TEXT,
            interests TEXT,
            experience TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS careers (
            career_id INTEGER PRIMARY KEY AUTOINCREMENT,
            career_name TEXT,
            description TEXT,
            required_skills TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            career_field TEXT,
            required_skills TEXT,
            level TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            job_id INTEGER,
            status TEXT
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM careers")
    if cursor.fetchone()[0] == 0:
        careers = [
            ("Data Analyst", "Analyze data and share insights.", "Python, SQL, Excel"),
            ("Software Engineer", "Build software and debug code.", "Python, JavaScript, Git"),
            ("Marketing Coordinator", "Help with marketing plans and social media.", "Writing, SEO, Design"),
            ("Graphic Designer", "Create images and visual content.", "Photoshop, Creativity, Layout")
        ]
        cursor.executemany(
            "INSERT INTO careers (career_name, description, required_skills) VALUES (?, ?, ?)",
            careers
        )

    cursor.execute("SELECT COUNT(*) FROM jobs")
    if cursor.fetchone()[0] == 0:
        jobs = [
            ("Junior Data Analyst", "TechCorp", "Data", "Python, SQL, Excel", "Entry"),
            ("Web Developer", "BrightApps", "Software", "Python, JavaScript, HTML", "Entry"),
            ("Marketing Assistant", "BrandFlow", "Marketing", "Writing, SEO, Social Media", "Entry")
        ]
        cursor.executemany(
            "INSERT INTO jobs (title, company, career_field, required_skills, level) VALUES (?, ?, ?, ?, ?)",
            jobs
        )

    conn.commit()
    conn.close()


def create_user(name, age, education, skills, interests, experience):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, age, education, skills, interests, experience) VALUES (?, ?, ?, ?, ?, ?)",
        (name, age, education, skills, interests, experience)
    )
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id


def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def get_user_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def update_user_profile(user_id, skills, interests):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET skills = ?, interests = ? WHERE user_id = ?",
        (skills, interests, user_id)
    )
    conn.commit()
    conn.close()


def get_all_careers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM careers")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_all_jobs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def insert_application(user_id, job_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applications (user_id, job_id, status) VALUES (?, ?, 'Applied')",
        (user_id, job_id)
    )
    conn.commit()
    conn.close()


def get_user_applications(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT a.application_id, a.status, j.title, j.company FROM applications a JOIN jobs j ON a.job_id = j.job_id WHERE a.user_id = ?",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
