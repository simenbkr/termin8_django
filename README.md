## termin8_django backend

Setting up the backend on your local machine:

Note: We are using Python2.7 with django and djangorestframework.
Install the following dependencies (using i.e. pip or another package manager):

    django
    djangorestframework
    mysql-python

Then clone this repo to your local machine:

    git clone git@github.com:simenbkr/termin8_django.git

Now it should be good to go, using the central database at termin8er (the RPi with domain termin8.tech).
To run the local dev server:

    cd termin8_django
    python manage.py runserver

Note: To get any specific branch (i.e. dev) do the following:

    git fetch
    git checkout <branchname>

To create a new branch and push it to github/origin:

    git branch <newbranchname>
    <do some coding>
    git add <files>
    git commit -m "<message>"
    git push -u origin <newbranchname>

Please report any issues on Slack or in the issues tab above.


#Usage
Current endpoints (base_url/api/`endpoint`):

    plant
    planttype
    wateringhistory
    sensorhistory
    room

These are following the REST standard - i.e. sending a GET request to base_url/api/plant will return all plants (that the user you are authenticated as can access). Sending a PUT-request to base_url/api/plant/`id` will update the plant with the JSON-object that was PUT (if accepted/valid).

To authenticate send a POST request with username and password to `base_url/auth/`. 
