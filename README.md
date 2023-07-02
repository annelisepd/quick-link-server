> ## Windows Guide
>
>```bash
>git clone git@github.com:RosyMaple/DjangoServer.git
>```
>
>```bash
>cd DjangoServer
>python -m venv venv
>venv\Scripts\activate
>pip install -r requirements
>```
>
>```bash
>setx DJANGO_SECRET "secret_key"
>setx DJANGO_HOST "www.host.com"
>```
>
>```bash
>setx DB_NAME "server_db"
>setx DB_USER "root"
>setx DB_PASSWORD "root"
>setx DB_HOST "127.0.0.1"
>setx DB_PORT "3306"
>```