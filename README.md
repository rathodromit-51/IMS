# Internship Management System (IMS)

A web-based Internship Management System built using Django that helps students discover internship opportunities, apply online, and manage their internship applications.

---

## 📌 Features

### Student Features
- User Registration & Login
- Student Profile Management
- Upload Resume
- Upload Profile Picture
- Browse Internship Positions
- Search Internships by Title
- Filter Internships by Location
- Apply for Internships
- View Applied Internships

### Company Features
- View Company List
- Company Profile
- View Available Internship Positions

### Internship Features
- Internship Details
- Internship Status (Open / Closed / Filled)
- Stipend Information
- Internship Duration
- Application Tracking

### Authentication
- User Registration
- Login
- Logout

---

## 🛠 Technologies Used

Backend
- Python
- Django
- SQLite

Frontend
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons

Database
- SQLite (Default Django Database)

---

## 📂 Project Structure

```
internship_management_system/
│
├── internships/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│
├── static/
│   └── css/
│       └── style.css
│
├── media/
│
├── manage.py
└── README.md
```

---

## Database Models

### Company
- Name
- Email
- Website
- Location
- Description

### Student
- User
- Roll Number
- Degree
- Branch
- Semester
- GPA
- Phone
- Resume
- Profile Picture
- Skills

### Internship Position
- Title
- Company
- Description
- Requirements
- Duration
- Stipend
- Location
- Status
- Start Date
- End Date

### Application
- Student
- Internship Position
- Cover Letter
- Resume
- Application Status

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/internship-management-system.git
```

### Move into Project

```bash
cd internship-management-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

## Screens

- Home Page
- Internship Listings
- Internship Details
- Company List
- Company Details
- Student Profile
- Login
- Register
- Apply Internship

---

## Future Improvements

- Company Login
- Admin Dashboard
- Email Notifications
- Resume Parsing
- Internship Recommendation
- Interview Scheduling
- Search by Skills
- Pagination
- REST API
- Docker Deployment

---

## Author

**Romit S. Rathod**

Bachelor of Computer Applications (BCA)

Python | Django | SQL | HTML | CSS | Bootstrap

GitHub:
[https://github.com/rathodromit-51
](https://github.com/rathodromit-51)
LinkedIn:
[https://linkedin.com/in/yourprofile
](https://www.linkedin.com/in/romit-rathod-098a30283/)

---

## License

This project is created for educational purposes.
