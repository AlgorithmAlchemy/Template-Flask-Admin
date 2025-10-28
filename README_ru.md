# Flask Admin Template

Простой шаблон Flask-приложения с подключённой админкой на Flask-Admin и SQLite.

---

## Стек технологий

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Admin](https://flask-admin.readthedocs.io/)
- SQLite (встроенная БД)

---

## Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/AlgorithmAlchemy/Flask-Admin-Template.git
cd Flask-Admin-Template
````
<p align="left">
  <img src="https://github.com/user-attachments/assets/f6759825-6203-45e8-b394-44275be372c6" alt="dd_DeWatermark" width="500" />
</p>



### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

Если `requirements.txt` нет — вручную:

```bash
pip install flask flask_sqlalchemy flask_admin
```

### 3. Запустить приложение

```bash
python app.py
```

### 4. Открыть в браузере

```
http://127.0.0.1:5000/admin
```

---

## Структура проекта

```
├── app.py                # Основной файл приложения Flask
├── mydatabase.db         # SQLite база (создаётся автоматически)
├── README.md             # Документация
└── .gitignore            # Исключения Git
```

--- 

## Описание

Приложение демонстрирует:

* создание таблицы `User` с полями `id`, `name`, `email`
* автоматическую генерацию админки через Flask-Admin
* подключение темы `cerulean` через `FLASK_ADMIN_SWATCH`

---

## Скриншот

*(Скрин админки)*

---

## License

MIT License © AlgorithmAlchemy

