import sqlite3

def initialize_db():
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        email TEXT PRIMARY KEY,
        names TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        name TEXT,
        trimester TEXT,
        credits REAL,
        PRIMARY KEY (name, trimester)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registrations (
        student_email TEXT,
        course_name TEXT,
        trimester TEXT,
        grade REAL,
        FOREIGN KEY (student_email) REFERENCES students (email),
        FOREIGN KEY (course_name, trimester) REFERENCES courses (name, trimester)
    )
    ''')

    conn.commit()
    conn.close()

def add_student(email, names):
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO students (email, names)
    VALUES (?, ?)
    ''', (email, names))
    conn.commit()
    conn.close()

def add_course(name, trimester, credits):
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO courses (name, trimester, credits)
    VALUES (?, ?, ?)
    ''', (name, trimester, credits))
    conn.commit()
    conn.close()

def register_student_for_course(student_email, course_name, trimester, grade):
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO registrations (student_email, course_name, trimester, grade)
    VALUES (?, ?, ?, ?)
    ''', (student_email, course_name, trimester, grade))
    conn.commit()
    conn.close()

def get_students():
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students

def get_courses():
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    conn.close()
    return courses

def get_student_courses(student_email):
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT courses.name, courses.trimester, courses.credits, registrations.grade
    FROM registrations
    JOIN courses ON registrations.course_name = courses.name AND registrations.trimester = courses.trimester
    WHERE registrations.student_email = ?
    ''', (student_email,))
    student_courses = cursor.fetchall()
    conn.close()
    return student_courses
