# Sup dear!

Blog developed with Django, MySql, Bootstrap4. 
See my video below (portuguese)

[Youtube video](https://youtu.be/ZfHioI0azKU)

## First Step

Install dependencies project, find in requirements.txt


Change your mysql instance and schema values in the blog/settings.py

    DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', # don't change this
    'NAME': 'blogdb',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': PASSWORD,
    }
    }

Run the command 

    python manage.py migrate

Now, set a superuser for your project, run the command and set your profile

    python manage.py createsuperuser



## See the application

Run the command:

    python manage.py runserver

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```
