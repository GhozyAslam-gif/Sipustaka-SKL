import os
import sys


path = '/home/GhozyAslam/perpus'  
if path not in sys.path:
    sys.path.insert(0, path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'perpus.settings'

# 3. Jalankan aplikasi WSGI Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()