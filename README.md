# space_django 

https://www.spacextrack.com/

## Development Server Setup

#### 1. Clone repo and cd into it
```
git clone --recursive https://github.com/jdineen21/space_django
cd space_django
```

#### 2. Create and mount python virtual environment
```
pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install required python packages from requirements.txt
```
pip install -r requirements/development.txt
```

#### 4. Install node modules and compile js
```
npm i
npm run production
```

#### 5. Create .env file from .env.example and insert secret key
```
cp .env.example .env
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' >> .env
```

#### 6. Launch django dev server
```
python manage.py runserver
```

## Deployment

#### 1. Perform System Check
```
python manage.py check --deploy --settings=space_django.settings.production
```

## pip Tips
Show outdated packages
```
pip list --outdated --format=freeze
```