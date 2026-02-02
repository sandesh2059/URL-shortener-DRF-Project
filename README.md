# URL-shortener
This is a DRF based url shortener web-app. 
It demonstrates RESTful API Development, CRUD operations, Authentication and proper project structure.
---

## Features
- User Registration and Login/Logout
- CRUD APIs (Create, Read, Update, Delete)
- RESTful API design
- Django Admin Panel
- sqlite support.
---

## Tech Stack
- python==3.12
- asgiref==3.11.0
- Django==6.0.1
- djangorestframework==3.16.1
- sqlparse==0.5.5
---

## Project Structure

```text
URLshortener/
│── URLshortener/
│   │── settings.py
│   │── urls.py
│── accounts/
│   │── models.py
│   │── forms.py
│   │── views.py
│   │── urls.py
│── shortener/
│   │── models.py
│   │── permissions.py
│   │── serializers.py
│   │── urls.py
│   │── utils.py
│   │── views.py
│── templates/
│   │── home.html
│   │── login.html
│   │── longurl.html
│   │── register.html
│── manage.py
│── README.md
```

---

## Installation and Setup
### 1. clone the repository
```bash
git clone https://github.com/sandesh2059/URL-shortener-DRF-Project.git
cd URL-shortener-DRF-Project
```
### 2. create virtual environment
```bash
python3 -m venv myenv
```

### 3. Activate virtual environment
```bash
sourve myenv/bin/activate
```

### 4. Install requirements
```bash
pip install django
pip install djangorestframework
```
### 5. Appy migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. create super user
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```


