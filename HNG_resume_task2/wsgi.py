"""
WSGI config for HNG_resume_task2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

#from HNG_resume_task2 import MyWSGIApp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HNG_resume_task2.settings')

application = get_wsgi_application()


#application = MyWSGIApp()
application = WhiteNoise(application, root='/path/to/static/files')
application.add_files('/path/to/more/static/files', prefix='more-files/')

