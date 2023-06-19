# Django Starter Blog

A simple blog application created using Django, Vue.js and GraphQL.

## Features

- Including recent posts, category, tag, and post page
- User registration and login. Built with JWT and Vuex (migrated to Pinia, which is the recommended package for stores).
- Comment section. Only authenticated users can leave comment, and it won’t show up until approved by the admin.
- User profile page. Guest user can see and edit all comments that belong to that user.
- Like system. Guest user can like posts and comments.


## Installation

For the backend, first create a virtual environment.

```bash
cd backend
python3 -m venv env
source env/bin/activate
```

Install required packages.

```bash
pip install -r requirements.txt
```

Run migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

If you get this error: `ImportError: cannot import name 'force_text' from 'django.utils.encoding'`, you can replace `force_text` with `force_str` like [this article](https://exerror.com/importerror-cannot-import-name-force_text-from-django-utils-encoding/). This issue should be resolved in future versions of Django.

Start dev server.

```bash
python manage.py runserver
```

For the frontend, install packages.

```bash
cd frontend
npm install
```

If you are getting errors when installing packages, just run `npm install --force`. Some packages has been deprecated, but everything still work for now. I will try to update this project as soon as possible.

Start frontend dev server.

```bash
npm run serve
```
