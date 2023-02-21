# Django DropBox API Project

This is a Django project that uses the DropBox API and Python SDK to display folders in the current DropBox folder.

## Project Structure

├── dropboxtest
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp
│   ├── admin.py
|   ├── apss.py
|   ├── models.py
|   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates
│   └── index.html
├── your_token.pickle
├── dropbox_auth.py
├── requirements.txt
├── manage.py
└── README.md


- `dropboxtest`: This is the main Django app that contains the settings, views, and URL configurations.
- `myapp`: This is the app that contains the views, and URL configurations that will display the folders in user's Dropbox .
- `templates`: This directory contains the HTML templates used to display the folders and files.
- `.env`: This file stores the user's Dropbox API access token.
- `your_token.pickle`: This file stores the user's Dropbox API access token.
- `authenticate.py`: This is a Python script that handles the Dropbox API authentication and authorization process.
- `requirements.txt`: This file contains the Python packages required to run the project.
- `manage.py`: This is the Django project management script.

## Functionality

The project uses the DropBox API and Python SDK to authenticate and authorize the user, and then display the folders in the user's current Dropbox folder. The user must first authorize the application to access their Dropbox account by running the authenticate script, after which the application retrieves the user's access token and saves it in a `your_token.pickle` file.

Once the user is authenticated, the application displays a list of folders and files in the user's Dropbox folder. The app has been done in Django for scalability, additional functionality such
as opening up the folder and redirecting the user to it can be added by adding a new view. The approach here is to create the base app with the barebones functionality that could be improved upon. This is just a simple app, but we can use the Dropbox client object to perform many different actions with the Dropbox API, such as uploading and downloading files, creating folders, and sharing files by simply incorporating the views or different apps depending on use case.

To run the project, clone the repository, install the required Python packages `pip install -r requirements.txt` from `requirements.txt`, and run `python manage.py runserver`. Enter your dropbox details and run the authenticate script `python authenticate.py`. Access the application at `http://localhost:8000/`.
