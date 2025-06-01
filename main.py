import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    all_passes = Passcard.objects.all()
    active_passes = Passcard.objects.filter(is_active=True)
    print('Всего пропусков ', len(all_passes))
    print('Активных пропусков ', len(active_passes))
