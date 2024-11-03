# clear_model_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'database.settings')
django.setup()

from mypage.models import creativereser, peer1reser, peer2reser, peer3reser

def clear_data():
    creativereser.objects.all().delete()
    peer1reser.objects.all().delete()
    peer2reser.objects.all().delete()
    peer3reser.objects.all().delete()
    print("Data cleared successfully.")

if __name__ == "__main__":
    clear_data()
