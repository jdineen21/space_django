# space_django 

https://www.spacextrack.com/

## Docker Development Server Setup

#### 1. Create and mount python virtual environment
  - virtualenv --python=python3 --always-copy .venv/
  - source .venv/bin/activate

#### 2. Install required python packages from requirements.txt
  - pip install -r requirements.txt

#### 3. Install node modules and compile js
  - npm i
  - npm run production

#### 4. Create .env file from .env.example and insert secret key
  - cp .env.example .env
  - python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' >> .env

#### 5. Launch docker container
  - docker-compose up

#### 6. Launch django dev server
  - python manage.py runserver