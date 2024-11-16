# management/commands/load_rental_codes.py
from django.core.management.base import BaseCommand
from user.models import RentalCode

class Command(BaseCommand):
    help = 'Load initial rental codes'
    
    def handle(self, *args, **kwargs):
        codes = [
            "0000", "1111", "2222", "3333", "4444", 
            "5555", "6666", "7777", "8888", "9999", 
            "1010", "2020", "3030", "4040", "5050", 
            "6060", "7070", "8080", "9090", "1122", 
            "2233", "3344", "4455", "5566", "6677", 
            "7788", "8899", "9900", "1234", "5678", 
            "1357", "2468"]

        
        # 기존 반환 코드 모두 삭제 (원하는 경우)
        RentalCode.objects.all().delete()

        for code in codes:
            RentalCode.objects.get_or_create(code=code)
        self.stdout.write(self.style.SUCCESS('Successfully loaded return codes.'))