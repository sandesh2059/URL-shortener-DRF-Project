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

### 8. enter the url in browser
```bash
localhost:8000/register
```

## Other functions of the app

1. users can register themselves
2. users can login using their username and password
3. users can logout
4. users can see all the already existing urls created by different users
5. users can create their own urls but they need special permission from admin
6. users can manually give the short url for their long urls
7. users with permission can perform CRUD operations to their urls
8. users can visit the long url using short url via user interface
    OR
```bash
localhost:8000/shortener/short-url
```

