
# 📝 Django Blog Web App

A full-featured **Blog Web Application** built using the **Django framework**. This project allows users to register, log in, create, edit, and delete blog posts. It also includes user authentication, responsive design, and a clean UI.

> 🔗 [View the Repository](https://github.com/IkramAlgo/Django-Blog-Web-App)

---

## 📌 Features

* User registration and authentication
* Create, update, and delete blog posts
* View posts by specific users
* Mobile-responsive and user-friendly interface
* Django Admin panel for backend management
* Reusable templates and components
* Pagination and SEO-friendly URLs

---

## 🛠️ Tech Stack

* **Backend**: Django, Python
* **Frontend**: HTML5, CSS3, Bootstrap
* **Database**: SQLite (default)
* **Deployment**: Ready for deployment on Linux servers using Apache/Mod\_WSGI or Gunicorn/Nginx

---

## 🚀 Getting Started

Follow these instructions to set up the project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/IkramAlgo/Django-Blog-Web-App.git
cd Django-Blog-Web-App
```

### 2. Set up a virtual environment

```bash
conda creater -n django_env python==3.10
conda activate django_env   
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (admin account)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🖥️ Admin Panel

Access the admin interface at:
`http://127.0.0.1:8000/admin/`

Use the credentials created with `createsuperuser` to log in and manage posts, users, etc.

---

## 📂 Project Structure

```
Django-Blog-Web-App/
│
├── blog/              # Blog app (core logic and views)
├── users/             # User registration & profile
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── media/             # Uploaded images (user profile pics)
├── manage.py          # Django project management script
├── db.sqlite3         # SQLite database
└── requirements.txt   # Python dependencies
```


## 🛠️ Future Improvements

* Add comments functionality
* Add tags/categories to blog posts
* Integrate a rich text editor for post creation
* Add REST API using Django REST Framework
* Deploy to a cloud platform (Heroku, Render, or Linode)

---

## 📬 Contact

If you have any questions or suggestions, feel free to contact me:

**Ikram Khan**
📧 [developerikram@gmail.com](mailto:developerikram@gmail.com)
🔗 [GitHub Profile](https://github.com/IkramAlgo)



## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

