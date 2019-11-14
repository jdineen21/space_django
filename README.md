# space_django 

https://www.spacextrack.com/

### To get development server running

#### Linux

1. virtualenv --python=python3 --always-copy .venv/

2. source .venv/bin/activate

3. pip install -r requirements.txt

4. npm i

5. npm run production

6. cp .env.example .env

7. python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' >> .env

8. (optional) python manage.py migrate

9. (optional) python manage.py createsuperuser

10. python manage.py runserver 