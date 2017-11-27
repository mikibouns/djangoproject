from subprocess import call
import os

path = 'D:\IGOR\PYTHON\DJANGO_PROJ\Scripts\python'
runserver = '{} manage.py runserver'.format(path)

if __name__ == '__main__':
    call(runserver, shell=True)
