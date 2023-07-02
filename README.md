> ## Windows Configuration Guide
>
>```bash
>git clone https://github.com/RosyMaple/QuickLink.git
>```
>
>```bash
>cd QuickLink
>python -m venv venv
>venv\Scripts\activate
>pip install -r requirements.txt
>```
>
>```bash
>setx DJANGO_SECRET "secret_key"
>setx DJANGO_HOST "www.quicklink.com"
>setx DJANGO_DEBUG "False"
>```
>
>```bash
>setx DB_NAME "server_db"
>setx DB_USER "root"
>setx DB_PASSWORD "root"
>setx DB_HOST "127.0.0.1"
>setx DB_PORT "3306"
>```
>```bash
>cd server
>python manage.py makemigrations
>python manage.py migrate
>python manage.py runserver
>```