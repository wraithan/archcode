from paver.easy import *
import paver.virtual
import os

base = path(os.path.abspath(os.path.dirname(__file__)))
easy_install = base + '/bin/easy_install'

libraries = [
    ('django', ''),
    ('django_registration', '-Z'),
]

options(
    virtualenv=Bunch(
        script_name='bootstrap.py',
        paver_command_line=('update_libraries'),
    ),
)

@task
def update_libraries():
    """Get and install libraries"""
    for lib in libraries:
        sh('%s %s %s' % (easy_install, lib[1], lib[0]))
