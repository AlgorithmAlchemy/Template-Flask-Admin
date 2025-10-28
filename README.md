# Flask Admin Template

A simple Flask application template with an integrated admin panel built using Flask-Admin and SQLite.

---

## Tech Stack

* [Flask](https://flask.palletsprojects.com/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
* [Flask-Admin](https://flask-admin.readthedocs.io/)
* SQLite (built-in database)

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/AlgorithmAlchemy/Flask-Admin-Template.git
cd Flask-Admin-Template
```

<p align="left">
  <img src="https://github.com/user-attachments/assets/f6759825-6203-45e8-b394-44275be372c6" alt="dd_DeWatermark" width="500" />
</p>

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing — install manually:

```bash
pip install flask flask_sqlalchemy flask_admin
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/admin
```

---

## Project Structure

```
├── app.py                # Main Flask application file
├── mydatabase.db         # SQLite database (created automatically)
├── README.md             # Documentation
└── .gitignore            # Git ignore rules
```

---

## Description

This application demonstrates:

* Creating a `User` table with fields `id`, `name`, `email`
* Automatic admin interface generation using Flask-Admin
* Applying the `cerulean` theme via `FLASK_ADMIN_SWATCH`

---

## Screenshot

*(Admin panel screenshot)*

---

## License

MIT License © AlgorithmAlchemy
