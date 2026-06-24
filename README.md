# CareerCompass – Smart Career Discovery & Job Recommendation System

## Project Description

CareerCompass is a Python desktop application that helps students, graduates, and job seekers discover suitable career paths and find matching jobs or internships. The system uses user interests, skills, and experience to generate career recommendations and job matches.

The system is built using Object-Oriented Programming (OOP), a Tkinter graphical user interface, and SQLite database storage for managing user profiles, career recommendations, job opportunities, and application tracking.

---

## Project Goal

The goal of this project is to create a career guidance system that:

* Helps users discover suitable career paths
* Recommends jobs and internships based on skills and interests
* Tracks job applications
* Identifies skill gaps for career improvement
* Demonstrates proper Python software architecture using OOP, GUI, and database integration

---

## End Goal (Project Completion Criteria)

The project is considered complete when:

* Users can create and manage profiles
* The career quiz generates accurate career recommendations
* Job recommendations are generated based on user skills
* Match scores are calculated correctly
* Application statuses can be tracked
* User data is stored and retrieved using SQLite
* The application runs without errors

---

## Features

* Career discovery quiz
* Career recommendation engine
* User profile management
* Job and internship recommendations
* Skill-based matching system
* Application tracking
* Skill gap analysis
* SQLite database integration
* Tkinter graphical user interface

---

## Project Structure

```text
CareerCompass/

├── main.py                 # Entry point of application

├── database.py             # SQLite database operations

├── career_engine.py        # Career recommendation logic

├── job_matcher.py          # Job matching algorithm

├── skill_gap.py            # Skill gap analysis

├── application_tracker.py  # Application tracking system

├── models.py               # Data models

├── requirements.txt        # Project dependencies

├── README.md               # Project documentation

├── LICENSE                 # MIT License file

├── career_compass.db       # SQLite database

├── data/
│   ├── careers.csv
│   ├── jobs.csv
│   └── questions.csv

├── gui/
│   ├── dashboard.py
│   ├── career_quiz.py
│   ├── recommendations.py
│   └── applications.py

└── venv/                   # Virtual environment (Not pushed to GitHub)
```

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CareerCompass.git

cd CareerCompass
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows (Git Bash)**

```bash
source venv/Scripts/activate
```

**Windows (CMD)**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

---

## Installing Dependencies from Scratch

```bash
pip install pandas
```

Then generate the requirements file:

```bash
pip freeze > requirements.txt
```

---

## Database (SQLite)

The system uses SQLite to store and manage data.

Stored data includes:

* User profiles
* Career information
* Job opportunities
* Application records

This allows users to access and manage their information efficiently.

---

## OOP Structure

### User Class

Handles user information:

* Name
* Skills
* Interests
* Experience

### Career Class

Handles career information:

* Career name
* Description
* Required skills

### Job Class

Handles job information:

* Job title
* Career field
* Required skills

### Application Class

Handles application records and status tracking.

---

## System Workflow

```text
User Registration
        ↓
Career Quiz
        ↓
Career Recommendation
        ↓
Profile Creation
        ↓
Job Matching
        ↓
Application Tracking
```

---

## Technologies Used

* Python
* Tkinter
* SQLite
* Pandas
* Object-Oriented Programming (OOP)

---

## Future Improvements

* Resume/CV analysis
* Machine learning recommendations
* AI career assistant
* Real-time job listings
* Mobile application support

---

## Running the Project

After setup is complete:

```bash
python main.py
```

---

## Author

**Nathan Kiprono**

Bachelor of Science in Computer Science

---

## License

This project is licensed under the MIT License.


