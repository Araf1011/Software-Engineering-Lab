# 🧑‍💻 Software Engineering Lab — Django Learning Repository

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Django%20REST%20Framework-API-A30000?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

<p align="center">
  <b>A practical learning repository for our Software Engineering Lab.</b>
  <br>
  <sub>Learning Django by building, testing, debugging, and improving one concept at a time.</sub>
</p>

---

## 📑 Table of Contents

| # | Section | What you'll find |
|:---:|:---|:---|
| 01 | 📌 [About](#-about-this-repository) | Purpose and learning philosophy |
| 02 | 🧠 [Learning Areas](#-what-we-are-learning) | Django, database, REST API and CRUD |
| 03 | 🏗️ [Architecture](#️-project-architecture) | Project structure and responsibilities |
| 04 | 🧩 [Data Model](#-data-model) | Student entity and database flow |
| 05 | 🌐 [API](#-current-api-endpoints) | Current routes and operations |
| 06 | 🔄 [API Flow](#-how-the-current-api-flow-works) | Request-to-response lifecycle |
| 07 | 🛠️ [Tech Stack](#️-technology-stack) | Tools and technologies |
| 08 | 🚀 [Setup](#-running-the-project-locally) | Run the project locally |
| 09 | 🧪 [Commands](#-useful-django-commands) | Common Django commands |
| 10 | 📚 [Method](#-learning-method) | How the lab is practiced |
| 11 | 🗺️ [Roadmap](#️-learning-roadmap) | Current and upcoming topics |
| 12 | 🧹 [Repository Hygiene](#-repository-hygiene) | Keeping the repository clean |
| 13 | ⚠️ [Development Notes](#️-development-notes) | Security and development notes |
| 14 | 🎯 [Purpose](#-purpose-of-this-repository) | Why this repository exists |

---

## 📌 About This Repository

> 🎓 **Academic Learning Repository**

This repository contains the practical work, experiments, and implementations from our **Software Engineering Lab**, with a current focus on **Django and backend web development**.

The goal is to understand **how Django works internally and how its components connect**, rather than simply memorizing commands.

### 🔗 Core Learning Flow

```text
📥 Request
   │
   ▼
🔗 URL Routing
   │
   ▼
👁️ View
   │
   ├──────────────► 🔄 Serializer
   │                      │
   ▼                      ▼
🗃️ Model ◄────────── Validation
   │
   ▼
🗄️ Database
   │
   ▼
📤 Response
```

> 💡 **Learning philosophy:** Keep the implementation simple enough to understand, then gradually make it more structured and production-ready.

---

## 🧠 What We Are Learning

### 🐍 Django Fundamentals

<table>
<tr>
<td width="50%">

**⚙️ Project Basics**

- Django project structure
- Django applications
- `manage.py`
- Settings & configuration
- URL routing
- Views
- Django Admin

</td>
<td width="50%">

**🗃️ Database Basics**

- Django Models
- Model fields
- Migrations
- Django ORM
- SQLite
- CRUD database operations

</td>
</tr>
</table>

### 🔌 REST API Development

| Concept | What we practice |
|:---|:---|
| 🔄 Serializers | Python/model data ↔ JSON-compatible data |
| 📡 HTTP | Understanding request methods |
| 📦 JSON | Request and response data |
| 🧩 CRUD | Create, Read, Update, Delete |
| 🖥️ API Views | Processing API requests |
| 🛡️ CSRF | Handling API-style requests |
| 🧰 DRF | Django REST Framework fundamentals |

### 🔄 CRUD at a Glance

| Operation | Method | Purpose |
|:---:|:---:|:---|
| 🟢 Create | `POST` | Add a student |
| 🔵 Read | `GET` | Retrieve student data |
| 🟡 Update | `PUT` | Update/replace data |
| 🟠 Partial Update | `PATCH` | Update selected fields |
| 🔴 Delete | `DELETE` | Remove a student |

---

## 🏗️ Project Architecture

> 🧭 **One Django project → Multiple Django applications → Separate responsibilities**

The repository currently contains **one Django project** with separate Django applications used for different learning areas.

### 📁 Repository Structure

```text
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
    ├── 📦 student/                         ← ⚙️ Django project
    │   ├── ⚙️ settings.py
    │   ├── 🔗 urls.py
    │   ├── 🚀 asgi.py
    │   └── 🚀 wsgi.py
    │
    ├── 📦 result/                          ← 🧩 Main learning/API app
    │   ├── 🗃️ models.py
    │   ├── 👁️ views.py
    │   ├── 🔄 serializer.py
    │   ├── 🛠️ admin.py
    │   ├── ⚙️ apps.py
    │   ├── 🧪 tests.py
    │   └── 📂 migrations/
    │
    └── 📦 registration/                    ← 📝 Registration app
        ├── 🛠️ admin.py
        ├── ⚙️ apps.py
        ├── 🗃️ models.py
        ├── 👁️ views.py
        └── 🧪 tests.py
```

### 🧭 Project vs Application

<table>
<thead>
<tr>
<th>🏷️ Type</th>
<th>📦 Component</th>
<th>🎯 Responsibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>⚙️ Project</td>
<td><code>student/</code></td>
<td>Global configuration, settings and root URL routing</td>
</tr>
<tr>
<td>🧩 Application</td>
<td><code>result/</code></td>
<td>Student data, serializers and REST API practice</td>
</tr>
<tr>
<td>🧩 Application</td>
<td><code>registration/</code></td>
<td>Registration-related functionality</td>
</tr>
<tr>
<td>🚀 Utility</td>
<td><code>manage.py</code></td>
<td>Django command-line management</td>
</tr>
<tr>
<td>🗄️ Database</td>
<td><code>db.sqlite3</code></td>
<td>Local development database</td>
</tr>
</tbody>
</table>

### 🔍 File Responsibilities

<table>
<tr>
<th>📄 File</th>
<th>🎯 Responsibility</th>
</tr>
<tr><td><code>settings.py</code></td><td>Project configuration, installed apps, middleware and database settings</td></tr>
<tr><td><code>urls.py</code></td><td>Maps incoming URLs to views</td></tr>
<tr><td><code>views.py</code></td><td>Receives requests and returns responses</td></tr>
<tr><td><code>models.py</code></td><td>Defines database models</td></tr>
<tr><td><code>serializer.py</code></td><td>Converts model/Python data into JSON-compatible representations</td></tr>
<tr><td><code>admin.py</code></td><td>Registers models with Django Admin</td></tr>
<tr><td><code>apps.py</code></td><td>Application configuration</td></tr>
<tr><td><code>migrations/</code></td><td>Tracks database schema changes</td></tr>
<tr><td><code>tests.py</code></td><td>Place for automated tests</td></tr>
</table>

---

## 🧩 Data Model

> 👨‍🎓 The current database exercise intentionally uses a small **Student** entity so that we can focus on Models, ORM, serialization and CRUD before introducing relationships.

### 🗃️ Student Entity

```text
┌──────────────────────────────────────┐
│             👨‍🎓 STUDENT             │
├──────────────────────────────────────┤
│ 🔑 id       → Auto-generated PK      │
│ 👤 name     → VARCHAR(255)           │
│ 🔢 roll     → INTEGER                │
│ 📚 section  → VARCHAR(20)            │
└──────────────────────────────────────┘
```

### 🐍 Django Model

```python
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    section = models.CharField(max_length=20)
```

### 🧱 Field Reference

| Field | Django Type | Purpose |
|:---|:---|:---|
| 🔑 `id` | Auto-generated | Unique primary key |
| 👤 `name` | `CharField(255)` | Student's name |
| 🔢 `roll` | `IntegerField` | Student roll number |
| 📚 `section` | `CharField(20)` | Student section |

### 🔄 Database Flow

```text
📥 API Request
      │
      ▼
👁️ View
      │
      ▼
🔄 Serializer
      │
      ▼
✅ Validation
      │
      ▼
🗃️ Student Model
      │
      ▼
🗄️ SQLite Database
      │
      ▼
📤 JSON Response
```

---

## 🌐 Current API Endpoints

> 📡 These are the routes currently implemented/documented in the project.

### 📊 Endpoint Overview

<table>
<thead>
<tr>
<th>🔧 Method</th>
<th>🔗 Endpoint</th>
<th>🎯 Operation</th>
</tr>
</thead>
<tbody>
<tr><td><strong>GET</strong></td><td><code>/student/</code></td><td>👥 Get all students</td></tr>
<tr><td><strong>GET</strong></td><td><code>/student/&lt;id&gt;/</code></td><td>👤 Get one student</td></tr>
<tr><td><strong>POST</strong></td><td><code>/creatstudent/</code></td><td>➕ Create student</td></tr>
<tr><td><strong>PUT</strong></td><td><code>/creatstudent/</code></td><td>✏️ Update student</td></tr>
<tr><td><strong>PATCH</strong></td><td><code>/creatstudent/</code></td><td>🩹 Partially update student</td></tr>
<tr><td><strong>DELETE</strong></td><td><code>/creatstudent/</code></td><td>🗑️ Delete student</td></tr>
</tbody>
</table>

### ➕ Create Student

```http
POST /creatstudent/
Content-Type: application/json
```

**Request body**

```json
{
  "name": "Araf",
  "roll": 101,
  "section": "A"
}
```

### 👥 Read Students

```http
GET /student/
GET /student/<id>/
```

### ✏️ Update / 🩹 Partial Update / 🗑️ Delete

```http
PUT    /creatstudent/
PATCH  /creatstudent/
DELETE /creatstudent/
```

> 📝 **Implementation note:** The route is currently named `creatstudent/` in the project. It is documented exactly as implemented so that the README stays synchronized with the current code.

---

## 🔄 How the Current API Flow Works

### 🧠 Request Lifecycle

```text
             🌐 CLIENT
                 │
                 │ HTTP Request
                 ▼
          ┌─────────────┐
          │  🔗 urls.py │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │ 👁️ views.py │
          └──────┬──────┘
                 │
          ┌──────┴──────┐
          ▼             ▼
   ┌────────────┐  ┌────────────┐
   │ 🔄 Serializer│  │ 🗃️ Model   │
   └──────┬─────┘  └──────┬─────┘
          │                 │
          └────────┬────────┘
                   ▼
             ┌───────────┐
             │ 🗄️ SQLite │
             └─────┬─────┘
                   │
                   ▼
             📤 JSON Response
                   │
                   ▼
              🌐 CLIENT
```

### 🔁 CRUD Lifecycle

```text
➕ CREATE ──► 🗃️ Model ──► 🗄️ Database
                                  │
👤 READ   ◄───────────────────────┤
                                  │
✏️ UPDATE ────────────────────────┤
                                  │
🗑️ DELETE ────────────────────────┘
```

---

## 🛠️ Technology Stack

<table>
<thead>
<tr>
<th>🧰 Technology</th>
<th>🎯 Role in This Lab</th>
</tr>
</thead>
<tbody>
<tr><td>🐍 <strong>Python</strong></td><td>Primary programming language</td></tr>
<tr><td>🟢 <strong>Django</strong></td><td>Backend web framework</td></tr>
<tr><td>🔌 <strong>Django REST Framework</strong></td><td>REST API and serialization practice</td></tr>
<tr><td>🗄️ <strong>SQLite</strong></td><td>Local development database</td></tr>
<tr><td>🌐 <strong>HTTP / JSON</strong></td><td>API communication format</td></tr>
<tr><td>🔧 <strong>Git & GitHub</strong></td><td>Version control and repository management</td></tr>
</tbody>
</table>

---

## 🚀 Running the Project Locally

### 1️⃣ Clone

```bash
git clone https://github.com/Araf1011/Software-Engineering-Lab.git
cd Software-Engineering-Lab
```

### 2️⃣ Enter the Django Project

```bash
cd "Software Engineering"
```

### 3️⃣ Create & Activate Virtual Environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```powershell
python -m venv venv
venv\Scripts\activate
```

### 4️⃣ Install Dependencies

> 📦 A `requirements.txt` is not currently committed.

```bash
pip install django djangorestframework
```

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Useful Django Commands

<table>
<tr>
<th>💻 Command</th>
<th>🎯 Purpose</th>
</tr>
<tr><td><code>django-admin startproject project_name</code></td><td>Create a Django project</td></tr>
<tr><td><code>python manage.py startapp app_name</code></td><td>Create a Django application</td></tr>
<tr><td><code>python manage.py makemigrations</code></td><td>Create migration files</td></tr>
<tr><td><code>python manage.py migrate</code></td><td>Apply migrations</td></tr>
<tr><td><code>python manage.py runserver</code></td><td>Start development server</td></tr>
<tr><td><code>python manage.py createsuperuser</code></td><td>Create an admin user</td></tr>
<tr><td><code>python manage.py shell</code></td><td>Open Django shell</td></tr>
<tr><td><code>python manage.py test</code></td><td>Run automated tests</td></tr>
</table>

---

## 📚 Learning Method

> 🔁 **Learn → Implement → Test → Debug → Improve → Commit**

```text
📖 Learn a concept
      ↓
⌨️ Implement it
      ↓
🧪 Test it
      ↓
🐛 Debug errors
      ↓
🔧 Refactor / improve
      ↓
📌 Commit to Git
      ↓
➡️ Move to the next concept
```

### 🎯 Why This Approach?

<table>
<tr>
<td>📖 <strong>Understand</strong><br><sub>Learn the concept before using it.</sub></td>
<td>⌨️ <strong>Practice</strong><br><sub>Implement it with actual code.</sub></td>
<td>🧪 <strong>Verify</strong><br><sub>Test and observe the result.</sub></td>
</tr>
<tr>
<td>🐛 <strong>Debug</strong><br><sub>Learn from errors instead of hiding them.</sub></td>
<td>🔧 <strong>Improve</strong><br><sub>Refactor as understanding grows.</sub></td>
<td>📌 <strong>Document</strong><br><sub>Keep the repository as a learning record.</sub></td>
</tr>
</table>

---

## 🗺️ Learning Roadmap

### 🟢 Foundation — Practiced

- [x] Django project setup
- [x] Django app structure
- [x] URL routing
- [x] Views
- [x] Models
- [x] SQLite database
- [x] Migrations
- [x] Django Admin
- [x] Django REST Framework basics
- [x] Serializers
- [x] JSON requests/responses
- [x] CRUD concepts
- [x] `GET`, `POST`, `PUT`, `PATCH`, `DELETE`

### 🟡 Next — In Progress / Upcoming

- [ ] Function-based views → Class-based views
- [ ] ModelSerializer
- [ ] Generic API views
- [ ] ViewSets & Routers
- [ ] Proper REST API structure
- [ ] Authentication
- [ ] Permissions
- [ ] User registration & login
- [ ] Foreign Keys
- [ ] Model relationships
- [ ] Filtering & searching
- [ ] Pagination
- [ ] Advanced validation
- [ ] Automated testing
- [ ] API documentation
- [ ] Frontend integration
- [ ] Deployment

### 🔵 Future — Advanced

- [ ] Production-ready project structure
- [ ] Environment-based configuration
- [ ] PostgreSQL
- [ ] API versioning
- [ ] Caching
- [ ] Background tasks
- [ ] CI/CD
- [ ] Monitoring & logging

> 📌 The checklist will evolve as the Software Engineering Lab progresses.

---

## 🧹 Repository Hygiene

### 🚫 Files That Should Not Be Committed

```text
__pycache__/
*.pyc
venv/
.env
```

### 📦 Recommended Repository Improvements

| File | Purpose |
|:---|:---|
| `.gitignore` | Prevent unnecessary/local files from being committed |
| `requirements.txt` | Record Python dependencies |
| `.env.example` | Document required environment variables without exposing secrets |

> 🧼 Keeping these files organized makes the project easier to clone, understand, and maintain.

---

## ⚠️ Development Notes

This repository is currently intended for **local development and academic learning**, not production deployment.

### 🔐 Before Public Deployment

Review:

```text
🔑 SECRET_KEY
🐞 DEBUG
🌐 ALLOWED_HOSTS
🗄️ Database configuration
🛡️ CSRF configuration
🔐 Environment variables
```

> 🚨 **Never publish a real production `SECRET_KEY` in a public repository.** If a real secret has already been committed, rotate it and move it to environment variables.

---

## 🎯 Purpose of This Repository

This repository is designed to become a **living record of our Software Engineering Lab journey**.

<table>
<tr>
<td align="center">📓<br><strong>Learning Log</strong></td>
<td align="center">🧪<br><strong>Experiments</strong></td>
<td align="center">💻<br><strong>Django Practice</strong></td>
<td align="center">📚<br><strong>Reference</strong></td>
</tr>
<tr>
<td align="center">🐛<br><strong>Debugging</strong></td>
<td align="center">🔄<br><strong>Implementation</strong></td>
<td align="center">🚀<br><strong>Growth</strong></td>
<td align="center">🧭<br><strong>Future Projects</strong></td>
</tr>
</table>

The code may start simple — **that's intentional**.

The purpose is to be able to look back later and see the progression from basic Django concepts to complete backend applications.

---

## 👨‍💻 Author

<p align="center">
  <b>MD Al Araf Hossain</b>
  <br>
  Computer Science & Engineering Student
  <br>
  International Islamic University Chittagong
  <br><br>
  <a href="https://github.com/Araf1011">
    <img src="https://img.shields.io/badge/GitHub-Araf1011-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

---

<p align="center">
  <b>🚀 Learning Django — one concept, one endpoint, one bug at a time.</b>
  <br>
  <sub>Built for learning • Experimenting • Debugging • Improving</sub>
</p>
