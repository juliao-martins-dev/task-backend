# Task Backend API

Backend service for **Task Dashboard** built with **Django REST Framework (DRF)**.
This project provides RESTful APIs to manage users and tasks, designed to be consumed by a **Next.js frontend**.

---

## 🚀 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **JWT Authentication (SimpleJWT)**
- **SQLite** (development)

---

## ✨ Features

- User authentication with **username & password**
- **JWT-based authentication** (access & refresh token)
- Public access for **read-only endpoints**
- Protected endpoints for **create / update / delete**
- Clean RESTful API design
- Ready to integrate with **Next.js frontend**

---

## 📂 Project Structure

```txt
.
├── core/          # Core configuration (settings, urls, auth)
├── tasks/         # Tasks app (models, serializers, views)
├── db.sqlite3     # SQLite database (dev only)
├── manage.py
└── README.md
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/juliao-martins-dev/task-backend.git
cd task-backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
```

---

## ⚙️ Environment Variables

Create a `.env` file (recommended):

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

---

## 🗄️ Database Migration

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## ▶️ Run Development Server

```bash
python manage.py runserver
```

API will be available at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication (JWT)

### Obtain Token

```http
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Response:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

### Refresh Token

```http
POST /api/token/refresh/

{
  "refresh": "<refresh_token>"
}
```

### Authorization Header

```http
Authorization: Bearer <access_token>
```

---

## 🔓 Permissions Strategy

| Action | Auth Required |
|------|---------------|
| GET (list, detail) | ❌ No |
| POST | ✅ Yes |
| PUT / PATCH | ✅ Yes |
| DELETE | ✅ Yes |

Implemented using:

```python
IsAuthenticatedOrReadOnly
```

---

## 📌 API Endpoints

### Root

```http
GET /
```

### Users

```http
GET /users/
```

### Tasks

```http
GET /tasks/
POST /tasks/
GET /tasks/{id}/
PUT /tasks/{id}/
DELETE /tasks/{id}/
```

---

## 🧠 Security Notes (Developer Level)

- Access tokens are **short-lived**
- Refresh tokens can be rotated
- API is **secure by default**
- Designed for **stateless authentication**
- HTTPS required in production

---

## 🌐 Frontend Integration

This backend is designed to work with:

- **Next.js App Router**
- JWT stored securely on frontend
- RESTful communication via `fetch` / `axios`

---

## 🛠️ Development Notes

- SQLite is used for development only
- Use PostgreSQL/MySQL in production
- Configure CORS properly before deployment

---

## 📜 License

This project is open-source and available for learning and development purposes.

---

## 👨‍💻 Author

**Julião Martins**  
Backend & Fullstack Developer

---

> This project is part of a fullstack learning journey combining **Django REST Framework** and **Next.js**.

