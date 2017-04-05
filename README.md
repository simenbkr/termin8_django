# termin8_django backend

Backend for the website and interfaces between frontend and main controller and database.


Setting up the backend on your local machine:

Note: We are using Python2.7 with django and djangorestframework.
Install the following dependencies (using i.e. pip or another package manager):

    django
    djangorestframework
    python-mysql

Then clone this repo to your local machine:

    git clone git@github.com:simenbkr/termin8_django.git

Now it should be good to go, using the central database at termin8er (the RPi with domain termin8.tech).
To run the local dev server:

    cd termin8_django
    python manage.py runserver

Please report any issues on Slack or in the issues tab above.
