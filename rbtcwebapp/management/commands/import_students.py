from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connections

class Command(BaseCommand):
    help = 'Import students from PostgreSQL and create Django users'

    def handle(self, *args, **kwargs):
        # Connect to the PostgreSQL database
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT student_name, gr_no, email FROM club_users')

            for row in cursor.fetchall():
                student_name, gr_number, email = row

                # Check if the user already exists
                if not User.objects.filter(username=student_name).exists():
                    # Create a new user
                    user = User.objects.create_user(
                        username=student_name,
                        password=str(gr_number)  # Use gr_number as the password
                    )
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f'User created: {student_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'User already exists: {student_name}'))
