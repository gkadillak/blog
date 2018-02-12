import logging
import os
import subprocess

# TODO: write a decorator that catches the CalledProcessError and sends an email to me
# TODO: record when the deploy went out
# TODO: record the IP address of who sent the request
PYTHON_PATH = '/home/gkadillak/.virtualenvs/blog/bin/python'
PROJECT_ROOT = '/home/gkadillak/blog'

logger = logging.getLogger(__name__)

def log_exceptions(func):
    def wrapped_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            logger.error('%s: %s' % (e.__name__, e.output))
    return wrapped_func


@log_exceptions
def restart_gunicorn():
    subprocess.check_output('sudo /usr/sbin/service gunicorn restart'.split(' '))


@log_exceptions
def restart_nginx():
    subprocess.check_output('sudo /usr/sbin/service gunicorn restart'.split(' '), stderr=subprocess.STDOUT)


@log_exceptions
def pull_master():
    subprocess.check_output('git checkout master'.split(' '), stderr=subprocess.STDOUT)
    subprocess.check_output('git pull upstream master'.spit(' '))

@log_exceptions
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
