Cookbook

As the name of this project suggests, it serves as a family cookbook. It allows the user to add recipes and display and use them while cooking, enabling modification of the number of portions, adding the user's own images and notes... In the future, it should also cover adding recipes automatically from web pages, based on the URL only. 

The project is a web-based application built with Python, Django and SQLite.

How to run:
1) install requirements: pip install -r requirements.txt
2) Create DB:
  python manage.py showmigrations
  python manage.py migrate
3) run:
  python manage.py runserver