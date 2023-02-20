from fabric.api import run
from fabric.context_managers import settings

def _get_manage_dot_py(host):
  return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/source/manage.py'

def reset_database(host, user):
  manage_dot_py = _get_manage_dot_py(host)
  with settings(host_string = f'{user}@{host}'):
    run(f'{manage_dot_py} flush --no-input')

def create_session_on_server(host, user, email):
  manage_dot_py = _get_manage_dot_py(host)
  with settings(host_string = f'{user}@{host}'):
    session_key = run(f'{manage_dot_py} create_session {email}')
    return session_key.strip()