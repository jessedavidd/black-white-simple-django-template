# Black-and-white-Django-template
A simple website/blog template built using the Django framework.

## Features
- Simple blog functionality.
- Markdown editor for frontpage and for blog posts.
- Simple, mainly black and white colorscheme that is easily configurable.
- Google Analytics already built in. Just add your personal tracking code.

## How to use
Here is a short instruction list on how to get up and running with this blog template. 
After forking this repository, clone it to a desired location.
```
git clone https://github.com/jessedavidd/black-white-simple-django-template.git
cd black-white-simple-django-template
```
When the repoistory has successfully been cloned, cd into the repository. Now that you are in the project base directory, create a virtual python environment.
```
python -m venv venv
```
And then activate it...
```
source venv/bin/activate
```
When the virtual environment "venv" has successfully been activated, you need to install the requirements. These are found in the "requirements.txt" file. Install all requirements at once with the following command
```
pip install -r requirements.txt
```
Once the installation of the requrements is done, you need to migrate changes. 
```
python manage.py makemigrations
python manage.py migrate
```
At this point you have a working application! Let's make sure it works...
```
python manage.py runserver
```
Open your browser and navigate to: http://127.0.0.1:8000/
There you should see an empty blog waiting for you to configure it to your liking.

### Create a user and start configuring
To create a superuser for the site, use the following command:
```
python manage.py createsuperuser
```
and fill in the information.
The home page or "index" page is configured through the admin panel using Markdown. However, if you feel like you want to configure it using good old HTML, then just navigate to the `index.html` file which can be found at `main/templates/main/index.html` and delete the following:
```
{% for main in main_content %}
<p class="main-content-index">{{ main.content|safe_markdown }}</p>{% endfor %}
```
Now you're free to add whatever HTML you want.

### Configuring Google Analytics
Google Analytics functionality is made possible using the Django extension Django Google Analytics App.
To configure it, navigate to `BWDjangoTemplate/` and open `settings.py`.
In there edit the following section:
```
# Google analytics settings
GOOGLE_ANALYTICS = {
    'google_analytics_id': '#',
}
```
Change `#` to your personal Analytics tracking code.
