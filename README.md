# Spy Cat Agency - Backend

This is the backend for the Spy Cat Agency project.  
It is built with Django REST Framework (DRF).

---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/tumtu4/spy-cat-backend.git
```

2. **Clone the repository**
```bash
python -m venv .venv
.venv\Scripts\Activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Run migrations**
```bash
python manage.py migrate
```
5. **Run the server**
```bash
python manage.py runserver
```
Server will be available at:
```bash
http://127.0.0.1:8000
```

## API Endpoints
- **Spy Cats**
  - `GET` /api/cats/ — list all cats
  - `POST` /api/cats/ — create a new cat
  - `GET` /api/cats/{id}/ — get a single cat
  - `PATCH` /api/cats/{id}/ — update cat (only salary)
  - `DELETE` /api/cats/{id}/ — delete a cat

- **Missions**
  - `GET` /api/missions/ — list all missions
  - `POST` /api/missions/ — create a mission with targets
  - `GET` /api/missions/{id}/ — get a single mission
  - `PATCH` /api/missions/{id}/ — update mission or target
  - `DELETE` /api/missions/{id}/ — delete mission (only if not assigned to a cat)
  - `POST` /api/missions/{id}/assign_cat/ — assign a cat to mission

- **Targets**
  - `GET` /api/targets/ — list all targets
  - `GET` /api/targets/{id}/ — get single target
  - `PATCH` /api/targets/{id}/ — update target notes or completed status
  - `DELETE` /api/targets/{id}/ — delete a cat

## Postman

link: https://werdicer-9435790.postman.co/workspace/werdicer's-Workspace~17d386b2-39de-439f-846f-35e15d166bd6/collection/50866029-3f7afce9-57a0-49fa-bd15-45841746444e?action=share&creator=50866029

