# License Management System  

This is a Django + MySQL project forked and customized for managing **license categories, licenses, and jobs** with an admin dashboard.  

---

## 🔑 Features  
- Manage license categories & licenses  
- Job postings and applicant management  
- Django admin for easy management  
- User authentication & authorization  

---

## ⚙️ Setup  

1. Clone the repo  
   ```bash
   git clone <repo-url>
   cd license
   ```
2. Create & activate virtual environment
  ```bash
python -m venv venv
.\venv\Scripts\activate   # Windows PowerShell
  ```

3. Install dependencies
 ```bash
pip install -r requirements.txt
  ```

4. Configure MySQL in settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'license_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations & start the server
```bash
python manage.py migrate
python manage.py runserver
```

6. Access the site at:
```bash
Main site → http://127.0.0.1:8000/

Admin → http://127.0.0.1:8000/admin/
```
👩‍💻 Author

Forked & customized by Betty Jelagat
