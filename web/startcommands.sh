/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py collectstatic  --noinput
/usr/local/bin/gunicorn RA.wsgi:application -w 2 -b :8000
