## Development

> Tested with Python 3.6

Start dev server:
1. Run `source activate py36` if you are using virtual env, where py36 is an env with Python 3.6
2. Run DB migrations: `python manage.py migrate`
3. Start dev server: `python manage.py runserver`


Everytime a models is changed - run `python manage.py migrate ` and `python manage.py makemigrations polls`