# Django Admin Tester

I got tired of using random projects I had lying around to test out changes to
the Django admin, since they never had all fields I wanted to use and abuse.

This project depends on nothing but Django, and has models with every conceivable
field and modeladmins which expose these models in many possible ways.

Maybe one day it can serve as a "known quantity" for frontend JS tests. For
now it's just another yak shaved.

# Usage

1. Make sure you have some version of Django installed.
2. ./manage.py syncdb
3. ./manage.py runserver
4. [Go do things in the admin.](http://localhost:8000/admin)
