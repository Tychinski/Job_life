
python -m pip  install -r requirements.txt || exit 1
python manage.py makemigrations || exit 1
python manage.py migrate || exit 1
python manage.py collectstatic --noinput || exit 1

exec "$@"