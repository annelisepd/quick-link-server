# QuickLink 🔗

Welcome to QuickLink, your go-to Django project for effortless URL management. With QuickLink, you can create shortened links paired with unique keys that seamlessly redirect users to their desired destinations. Gone are the days of dealing with lengthy URLs – QuickLink simplifies and enhances your browsing experience.

## Features 🎯

- **Create Shortened Links:** User-friendly interface to generate shortened links for your desired URLs.
- **URL Redirection:** Direct users to the intended destinations by simply using the generated shortened links.
- **Tracking User Information:** QuickLink records essential information such as user agents and IP addresses for every access, providing valuable insights.

## Installation 🚀

To get started with QuickLink, follow these simple steps:

1. Clone this repository to your local machine.
2. Create and activate a virtual environment.
3. Install the project dependencies using `pip`.
4. Configure your database settings in `settings.py`.
5. Apply database migrations.
6. Launch the development server.

[Windows Configuration Guide](#windows-configuration-guide) | [Ubuntu Configuration Guide](#ubuntu-configuration-guide)

## Contributing 🤝

If you encounter any issues, have suggestions for improvements, or would like to contribute new features, feel free to submit a pull request. We welcome contributions and appreciate your interest in contributing to QuickLink! 💚

## Special Thanks 🙌

A big shoutout to [@WhitePoodleMoth](https://github.com/WhitePoodleMoth) for their valuable contribution to this project. Thank you for your dedication and commitment to QuickLink!

<br> ⬇ <br>

# Installation Guide ⚙️
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
>setx DJANGO_HOST "*"
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
>export DJANGO_SECRET="your private secret key"
>export DJANGO_HOST="*"
>export DJANGO_DEBUG="False"
>```
><sub>💭 In Ubuntu, if a string (e.g. your secret key) contains "$", it will throw an error. In case this happens with your generated key, simply replace the ocurrencies with any other character.</sub> <br>
> <sub>💡 Tip: Generate your secret key at https://djecrety.ir/ </sub> <br>
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
