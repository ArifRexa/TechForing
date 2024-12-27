# Project Management System

This project is a Django-based project management system with functionalities for managing projects, tasks, and members. It includes RESTful API endpoints for interacting with these resources.

## Features
- Create, retrieve, update, and delete projects.
- Assign tasks to projects and users.
- API documentation using DRF Spectacular.
- Authentication with Django REST Framework.

---

## Installation Instructions

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- SQLite for local development
- Git

### Step 1: Clone the Repository
```bash
$ git clone <repository_url>
$ cd <repository_directory>
```

### Step 2: Create and Activate a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
$ pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
$ python manage.py migrate
```

### Step 5: Create a Superuser
```bash
$ python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### Step 6: Start the Server
```bash
$ python manage.py runserver
```
Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---
## API Documentation

Below is the complete API reference for the project.

### **Users**
| Endpoint                       | Method | Description                              |
|--------------------------------|--------|------------------------------------------|
| `/api/users/register/`         | POST   | Create a new user                        |
| `/api/users/login/`            | POST   | Authenticate a user and return a token   |
| `/api/users/{id}/`             | GET    | Retrieve details of a specific user      |
| `/api/users/{id}/`             | PUT    | Update user details                      |
| `/api/users/{id}/`             | DELETE | Delete a user account                    |

### **Projects**
| Endpoint                       | Method | Description                              |
|--------------------------------|--------|------------------------------------------|
| `/api/projects/`               | GET    | Retrieve a list of all projects          |
| `/api/projects/`               | POST   | Create a new project                     |
| `/api/projects/{id}/`          | GET    | Retrieve details of a specific project   |
| `/api/projects/{id}/`          | PUT    | Update project details                   |
| `/api/projects/{id}/`          | DELETE | Delete a project                         |

### **Tasks**
| Endpoint                              | Method | Description                              |
|---------------------------------------|--------|------------------------------------------|
| `/api/projects/{project_id}/tasks/`   | GET    | Retrieve a list of all tasks in a project|
| `/api/projects/{project_id}/tasks/`   | POST   | Create a new task in a project           |
| `/api/tasks/{id}/`                    | GET    | Retrieve details of a specific task      |
| `/api/tasks/{id}/`                    | PUT    | Update task details                      |
| `/api/tasks/{id}/`                    | DELETE | Delete a task                            |

### **Comments**
| Endpoint                              | Method | Description                              |
|---------------------------------------|--------|------------------------------------------|
| `/api/tasks/{task_id}/comments/`      | GET    | Retrieve a list of all comments on a task|
| `/api/tasks/{task_id}/comments/`      | POST   | Create a new comment on a task           |
| `/api/comments/{id}/`                 | GET    | Retrieve details of a specific comment   |
| `/api/comments/{id}/`                 | PUT    | Update comment details                   |
| `/api/comments/{id}/`                 | DELETE | Delete a comment                         |

---
## API Documentation Access

API documentation is auto-generated using DRF Spectacular. Access it at:
- Swagger: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

