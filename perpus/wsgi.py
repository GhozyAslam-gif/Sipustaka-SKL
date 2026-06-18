import os
import sys

# Jalur direktori utama tempat proyek Anda berada
path = '/home/Ghozy/perpus'
if path not in sys.path:
    sys.path.insert(0, path)

# Mengarahkan ke file settings.py di dalam folder perpus Anda
os.environ['DJANGO_SETTINGS_MODULE'] = 'perpus.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()