# 🧑‍💻 Software Engineering Lab — Django Learning Repository

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Django%20REST%20Framework-API-A30000?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Learning-Project-8A2BE2?style=for-the-badge" alt="Learning Project">
</p>

<p align="center">
  <b>A practical collection of work, experiments, and implementations from our Software Engineering Lab.</b>
  <br>
  <sub>Learning Django by building — one concept at a time.</sub>
</p>

---

## 📌 About This Repository

This repository contains the code and practical work completed during our **Software Engineering Lab**, with a current focus on learning **Django** and backend web development.

The goal is not just to memorize Django commands, but to understand how a Django application is structured and how the different parts work together:

**Request → URL → View → Serializer/Model → Database → Response**

As the lab progresses, this repository will grow with new concepts, experiments, APIs, database operations, and mini-project implementations.

> 🎓 **Academic Learning Repository**  
> This is primarily a learning and lab-work repository. Code may evolve, be refactored, or intentionally remain simple while concepts are being learned.

---

## 🧠 What We Are Learning

### 🐍 Python & Django Fundamentals
- Django project structure
- Django applications
- \`manage.py\`
- Settings and configuration
- URL routing
- Views
- Models
- Django Admin
- SQLite database
- Database migrations

### 🗄️ Database & ORM
- Django Models
- Model fields
- Creating database tables through migrations
- Querying objects with Django ORM
- Creating, retrieving, updating and deleting records
- Working with SQLite

### 🔌 REST API Development
- Django REST Framework
- Serializers
- JSON serialization
- JSON parsing
- HTTP methods
- CRUD operations
- Request/response handling
- \`JSONRenderer\`
- \`JSONParser\`
- CSRF handling for API-style requests

### 🔄 CRUD Operations

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | \`POST\` | Add a new student |
| Read One | \`GET\` | Retrieve one student |
| Read All | \`GET\` | Retrieve all students |
| Update | \`PUT\` | Replace/update student data |
| Partial Update | \`PATCH\` | Update selected fields |
| Delete | \`DELETE\` | Remove a student |

---

## 🏗️ Project Architecture

The repository currently contains **one Django project** with separate Django applications.

### 📁 Repository Structure

\`\`\`text
📦 Software-Engineering-Lab
│
├── 📄 README.md
│
└── 📂 Software Engineering
    │
    ├── ⚙️ manage.py
    ├── 🗄️ db.sqlite3
    ├── 🐍 myapp.py
    │
    ├── 📦 student/                  ← Django project configuration
    │   ├── ⚙️ settings.py
    │   ├── 🔗 urls.py
    │   ├── 🚀 asgi.py
    │   └── 🚀 wsgi.py
    │
    ├── 📦 result/                   ← Main learning/API application
    │   ├── 🗃️ models.py
    │   ├── 👁️ views.py
    │   ├── 🔄 serializer.py
    │   ├── 🛠️ admin.py
    │   ├── ⚙️ apps.py
    │   ├── 🧪 tests.py
    │   └── 📂 migrations/
    │
    └── 📦 registration/             ← Registration-related application
        ├── 🛠️ admin.py
        ├── ⚙️ apps.py
        ├── 🗃️ models.py
        ├── 👁️ views.py
        └── 🧪 tests.py
\`\`\`

### 🧭 Project vs App

| Component | Role |
|---|---|
| 📦 student/ | Main Django project: configuration, settings and root URL routing |
| 📦 result/ | Main app used for student data, serializers and REST API practice |
| 📦 registration/ | Separate app reserved for registration-related work |
| ⚙️ manage.py | Command-line entry point for Django management tasks |
| 🗄️ db.sqlite3 | Local SQLite database |

### 🔍 File Responsibilities

| File | Responsibility |
|---|---|
| ⚙️ settings.py | Installed apps, middleware, database and project configuration |
| 🔗 urls.py | Maps incoming URLs to views |
| 👁️ views.py | Processes requests and creates responses |
| 🗃️ models.py | Defines database models |
| 🔄 serializer.py | Converts data between Python/model objects and JSON-compatible data |
| 🛠️ admin.py | Registers models with Django Admin |
| 📂 migrations/ | Tracks database schema changes |
| 🧪 tests.py | Space for automated tests |

## 🧩 Data Model

The current database exercise uses a simple **Student** entity. It is intentionally small so we can focus on Django Models, ORM operations, serialization and CRUD before introducing relationships.

### 👨‍🎓 Student

\`\`\`text
┌────────────────────────────────────┐
│          👨‍🎓  STUDENT             │
├────────────────────────────────────┤
│ 🔑 id       INTEGER     Primary Key│
│ 👤 name     VARCHAR(255)           │
│ 🔢 roll     INTEGER                │
│ 📚 section  VARCHAR(20)            │
└────────────────────────────────────┘
\`\`\`

### 🐍 Django Model

\`\`\`python
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    section = models.CharField(max_length=20)
\`\`\`

### 🧱 Field Reference

| Field | Type | Description |
|---|---|---|
| 🔑 id | Auto-generated | Unique primary key |
| 👤 name | CharField(255) | Student name |
| 🔢 roll | IntegerField | Student roll number |
| 📚 section | CharField(20) | Student section |

### 🔄 Data Flow

\`\`\`text
📥 Request
   ↓
🔄 Serializer
   ↓
✅ Validation
   ↓
🗃️ Student Model
   ↓
🗄️ SQLite
   ↓
📤 JSON Response
\`\`\`

This model is the foundation for the current **GET, POST, PUT, PATCH and DELETE** practice.

## 🌐 Current API Endpoints

The current project exposes the following routes:

### 👤 Get a Single Student

\`\`\`http
GET /student/<id>/
\`\`\`

Example:

\`\`\`http
GET /student/1/
\`\`\`

### 👥 Get All Students

\`\`\`http
GET /student/
\`\`\`

### ➕ Create a Student

\`\`\`http
POST /creatstudent/
\`\`\`

Example JSON:

\`\`\`json
{
  "name": "Araf",
  "roll": 101,
  "section": "A"
}
\`\`\`

### ✏️ Update a Student

\`\`\`http
PUT /creatstudent/
\`\`\`

### 🩹 Partially Update a Student

\`\`\`http
PATCH /creatstudent/
\`\`\`

### 🗑️ Delete a Student

\`\`\`http
DELETE /creatstudent/
\`\`\`

> **Note:** The route is currently named \`creatstudent/\` in the project. It is documented exactly as implemented so the README matches the current code.

---

## 🔄 How the Current API Flow Works

The current implementation follows this basic flow:

\`\`\`text
                HTTP Request
                     │
                     ▼
               ┌───────────┐
               │   urls.py │
               └─────┬─────┘
                     │
                     ▼
               ┌───────────┐
               │  views.py │
               └─────┬─────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    ┌─────────────┐       ┌──────────────┐
    │ serializer  │       │    models    │
    └──────┬──────┘       └──────┬───────┘
           │                     │
           └──────────┬──────────┘
                      ▼
                ┌───────────┐
                │  SQLite   │
                └─────┬─────┘
                      │
                      ▼
                JSON Response
\`\`\`

This architecture is intentionally kept simple so that the fundamentals are easy to understand before moving to more advanced Django patterns.

---

## 🛠️ Technology Stack

| Technology | Role |
|---|---|
| 🐍 **Python** | Programming language |
| 🟢 **Django** | Backend web framework |
| 🔌 **Django REST Framework** | REST API and serialization |
| 🗄️ **SQLite** | Development database |
| 🌐 **HTTP / JSON** | API communication |
| 🔧 **Git & GitHub** | Version control and collaboration |

---

## 🚀 Running the Project Locally

### 1️⃣ Clone the Repository

\`\`\`bash
git clone https://github.com/Araf1011/Software-Engineering-Lab.git
cd Software-Engineering-Lab
\`\`\`

### 2️⃣ Enter the Django Project

\`\`\`bash
cd "Software Engineering"
\`\`\`

### 3️⃣ Create a Virtual Environment

Linux/macOS:

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

Windows:

\`\`\`powershell
python -m venv venv
venv\\Scripts\\activate
\`\`\`

### 4️⃣ Install Dependencies

At the moment, the project does not include a committed \`requirements.txt\`. Install the required packages manually:

\`\`\`bash
pip install django djangorestframework
\`\`\`

### 5️⃣ Apply Migrations

\`\`\`bash
python manage.py migrate
\`\`\`

### 6️⃣ Start the Development Server

\`\`\`bash
python manage.py runserver
\`\`\`

Then open:

\`\`\`text
http://127.0.0.1:8000/
\`\`\`

---

## 🧪 Useful Django Commands

These are some of the commands we are using while learning Django:

\`\`\`bash
# Start a Django project
django-admin startproject project_name

# Create an application
python manage.py startapp app_name

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver

# Create an admin/superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Run tests
python manage.py test
\`\`\`

---

## 📚 Learning Method

The repository follows a **learn → implement → test → improve** workflow.

\`\`\`text
📖 Learn a concept
      ↓
⌨️ Implement it
      ↓
🧪 Test it
      ↓
🐛 Debug errors
      ↓
🔧 Improve/refactor
      ↓
📌 Commit to Git
      ↓
➡️ Move to the next concept
\`\`\`

Instead of building one huge application immediately, individual Django concepts are practiced first and then combined into larger features.

---

## 🗺️ Learning Roadmap

The repository will gradually move through topics such as:

### ✅ Currently Practicing

- [x] Django project setup
- [x] Django app structure
- [x] URL routing
- [x] Views
- [x] Models
- [x] SQLite database
- [x] Django migrations
- [x] Django Admin
- [x] Django REST Framework basics
- [x] Serializers
- [x] JSON requests/responses
- [x] CRUD API concepts
- [x] \`GET\`, \`POST\`, \`PUT\`, \`PATCH\`, \`DELETE\`

### 🔜 Upcoming Topics

- [ ] Function-based views → Class-based views
- [ ] ModelSerializer
- [ ] Generic API views
- [ ] ViewSets & Routers
- [ ] Proper REST API structure
- [ ] Authentication
- [ ] Permissions
- [ ] User registration/login
- [ ] Relationships between models
- [ ] Foreign Keys
- [ ] Filtering & searching
- [ ] Pagination
- [ ] Validation
- [ ] Automated testing
- [ ] API documentation
- [ ] Frontend integration
- [ ] Deployment
- [ ] Production-ready project structure

> The checklist is intentionally updated as the lab progresses.

---

## 🧹 Repository Hygiene

As this is an active learning repository, some generated development files may appear during local experimentation.

For a cleaner production-style repository, files such as these should generally be excluded from version control:

\`\`\`text
__pycache__/
*.pyc
venv/
.env
\`\`\`

A future cleanup can also introduce:

\`\`\`text
.gitignore
requirements.txt
.env.example
\`\`\`

This will make the repository easier for other students to clone and run.

---

## ⚠️ Development Notes

This project is currently configured for **local development**, not production deployment.

Before deploying a Django project publicly, review security settings such as:

- \`SECRET_KEY\`
- \`DEBUG\`
- \`ALLOWED_HOSTS\`
- database configuration
- CSRF configuration
- environment variables

**Important:** Never publish a real production \`SECRET_KEY\` in a public repository. If a real secret has already been committed, it should be rotated and moved to environment variables.

---

## 🎯 Purpose of This Repository

The main purpose of this repository is to keep a **living record of our Software Engineering Lab journey**.

It serves as:

- 📓 A personal learning log
- 🧪 A place for lab experiments
- 💻 A Django practice repository
- 📚 A reference for future topics
- 🔍 A record of implementation and debugging
- 🚀 A foundation for larger Django projects

The code may start simple — that's intentional.

The idea is to look back later and see how the project evolved from basic Django concepts into more complete backend applications.

---

## 👨‍💻 Author

**MD Al Araf Hossain**

Computer Science & Engineering Student  
International Islamic University Chittagong

- GitHub: [@Araf1011](https://github.com/Araf1011)

---

<p align="center">
  <b>Learning Django one endpoint at a time 🚀</b>
  <br>
  <sub>Built for learning • Experimenting • Improving</sub>
</p>
