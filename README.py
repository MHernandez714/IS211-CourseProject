#!/usr/bin/env python
# coding: utf-8

# In[ ]:



Below is a complete Flask blog application, including `app.py`, database models, templates, and a README.
You can copy these into your project files.


This project is a simple blog made with Flask. It lets a user log in, write posts, edit them, delete them, and see all posts on the main page. The goal is to show what was learned in class—how to use routes, templates, a database, and basic create/edit/delete actions.


When the app runs, Flask sets up a small SQLite database using SQLAlchemy. A user logs in on the `/login` page. After logging in, they go to the dashboard, where they can add new posts or manage the ones they already created. Each action uses a route that handles showing forms or saving changes.

All posts appear on the homepage, with the newest at the top. Each post has its own page that shows the title, author, date, and full text. The login system is simple and only for learning—passwords are not encrypted.


The app uses two models: `User` and `Post`. The `User` model stores basic login information. The `Post` model stores each blog entry and includes a title, content, author name, date posted, and a link to the user who created it. SQLAlchemy handles how data is saved and connected between users and posts.
markdown


This project is a simple blogging platform built using the Flask web framework. It allows a user to log in, create blog posts, edit them, delete them, and display all posts publicly on the home page. The goal of the application is to demonstrate core concepts learned in class, including routing, templates, database modeling, and CRUD operations.

When the application starts, Flask initializes the SQLite database using the SQLAlchemy ORM. The user can log in through the `/login` page, and once authenticated, they are redirected to the dashboard. From the dashboard, the user can create new posts, edit existing posts, or delete posts. Each action corresponds to a specific route in the application and uses POST and GET methods appropriately.

Posts are stored in the database and displayed on the homepage in reverse chronological order. Each post has a dedicated view page which displays the full content, author, and publication date. The login system is basic and designed for learning purposes, without encrypted passwords.


The application uses two database models: `User` and `Post`. The `User` model stores login credentials, while the `Post` model stores each blog entry. The `Post` model includes fields for title, content, author, timestamp, and a foreign key linking the post to the user who created it. SQLAlchemy manages the relationship between users and their posts, ensuring data is properly stored and retrieved.

