## Windows Configuration Guide
>
>### Previous Requirements:
> - Python
> - MySQL (Developer Default)
> - Git
>
>#### **1. Clone the Repository**
>```bash
>git clone https://github.com/RosyMaple/QuickLink.git
>```
>
>#### **2. Activate the Virtual Environment & Install the Needed Libraries**
>```bash
>cd QuickLink
>python -m venv venv
>venv\Scripts\activate
>pip install -r requirements.txt
>```
>
> #### **3. Set Global Variables to Django Settings**
>
>```bash
>setx DJANGO_SECRET "secret_key"
>setx DJANGO_HOST "quicklink.com"
>setx DJANGO_DEBUG "False"
>```
> <sub>💡 Tip: Generate your secret key at https://djecrety.ir/ </sub> <br>
> <br>
> #### **4. Set Global Variables to MySQL Database**
>  <sub>❕ Make sure to, first, create the "server_db" database with the user credentials below. </sub>
>```bash
>setx DB_NAME "server_db"
>setx DB_USER "root"
>setx DB_PASSWORD "root"
>setx DB_HOST "127.0.0.1"
>setx DB_PORT "3306"
>```
> #### **5. Run the Django Server**
>```bash
>cd server
>python manage.py migrate
>python manage.py makemigrations
>python manage.py runserver
>```

## Ubuntu Configuration Guide
>
>### Previous Requirements:
> - Python
> - MySQL (Developer Default)
> - Git
>
>#### **1. Clone the Repository**
>```bash
>git clone https://github.com/RosyMaple/QuickLink.git
>```
>
>#### **2. Activate the Virtual Environment & Install the Needed Libraries**
>```bash
>cd QuickLink
>python -m venv venv
>source venv/bin/activate
>pip install -r requirements.txt
>```
>
> #### **3. Set Global Variables to Django Settings**
> Open the **.bashrc** *or .bash_profile* file located in your home directory:
>```bash
> nano ~/.bashrc
> ```
> Add the following lines at the end of the file to set the environment variables:
>```bash
>export DJANGO_SECRET="secret_key"
>export DJANGO_HOST="quicklink.com"
>export DJANGO_DEBUG="False"
>```
><sub>💡 In Ubuntu, if a string (e.g. your secret key) contains "$", it will throw an error. In case this happens, replace the ocurrencies with any other character.</sub> <br>
> <br>
> #### **4. Set Global Variables to MySQL Database**
> In the .bashrc file, also add these lines: <br>
>  <sub>❕ Make sure to, first, create the "server_db" database with the user credentials below. </sub>
>```bash
>export DB_NAME="server_db"
>export DB_USER="root"
>export DB_PASSWORD="root"
>export DB_HOST="127.0.0.1"
>export DB_PORT="3306"
>```
> To save, press Ctrl + O and Enter. Then, Ctrl + X to exit the file. <br>
> For the changes to be applied, you need to restart the terminal or run the following command?
>```bash
> source ~/.bashrc
> ```
> #### **5. Run the Django Server**
>```bash
>cd server
>python manage.py migrate
>python manage.py makemigrations
>python manage.py runserver
>```