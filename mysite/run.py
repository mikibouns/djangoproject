from subprocess import call

if __name__ == '__main__':
    call('python manage.py runserver 0.0.0.0:8000', shell=True)
