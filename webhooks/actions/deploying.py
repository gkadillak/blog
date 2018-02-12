import os
import subprocess

# TODO: write a decorator that catches the CalledProcessError and sends an email to me
# TODO: record when the deploy went out
# TODO: record the IP address of who sent the request
PYTHON_PATH = '/home/gkadillak/.virtualenvs/blog/bin/python'
PROJECT_ROOT = '/home/gkadillak/blog'


def restart_gunicorn():
    subprocess.check_output('sudo /usr/sbin/service gunicorn restart'.split(' '), stderr=subprocess.STDOUT)


def restart_nginx():
    subprocess.check_output('sudo /usr/sbin/service gunicorn restart'.split(' '), stderr=subprocess.STDOUT)


def pull_master():
    subprocess.check_output('git checkout master'.split(' '), stderr=subprocess.STDOUT)
    subprocess.check_output('git pull upstream master'.spit(' '))


def collectstatic():
    command = '{PYTHON_PATH} manage.py collectstatic'.format(PYTHON_PATH=PYTHON_PATH)
    subprocess.check_output(command.split(' '), stderr=subprocess.STDOUT)


def move_to_project_root():
    os.chdir(PROJECT_ROOT)


def deploy_project():
    move_to_project_root()
    pull_master()
    collectstatic()
    restart_gunicorn()
    restart_nginx()
