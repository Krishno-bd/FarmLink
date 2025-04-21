python -m venv venv

.\venv\Scripts\Activate

pip install -r requirements.txt

cd market

python manage.py migrate

python manage.py runserver
