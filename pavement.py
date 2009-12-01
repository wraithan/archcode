from paver.easy import *
import paver.virtual

options(
    virtualenv=Bunch(
        script_name='bootstrap.py',
        packages_to_install=['Django', 'django-registration']
    )
)

