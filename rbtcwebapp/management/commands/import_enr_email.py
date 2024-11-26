from django.core.management.base import BaseCommand
from django.db import connections
from django.contrib.auth.models import User
from rbtcwebapp.models import Profile  # Replace with your Profile model if using one

class Command(BaseCommand):
    help = 'Import student enrollment numbers and emails from PostgreSQL into Django User and Profile models'

    def handle(self, *args, **kwargs):
        try:
            with connections['default'].cursor() as cursor:
                # Fetch only enrollment_no and email
                cursor.execute('SELECT enrollment_no, email, student_name FROM club_users')
                rows = cursor.fetchall()

                for row in rows:
                    if len(row) == 3:
                        enrollment_no, email, student_name = row
                    else:
                        self.stdout.write(self.style.ERROR(f"Row with unexpected number of columns: {row}"))
                        continue  # Skip if the row is not as expected

                    # Clean the student name
                    student_name = student_name.strip()

                    print(f"Trying to fetch or create user with username: {student_name}")

                    # Try fetching the user or create a new one if not found
                    user, created = User.objects.get_or_create(username=student_name)

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created new user: {student_name}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"User already exists: {student_name}"))

                    # Update the user's email
                    user.email = email
                    user.save()

                    # Update or create the profile with the enrollment number
                    profile, profile_created = Profile.objects.get_or_create(user=user)
                    profile.enrollment_number = enrollment_no
                    profile.save()

                    if profile_created:
                        self.stdout.write(self.style.SUCCESS(f"Created profile for: {student_name}"))
                    else:
                        self.stdout.write(self.style.SUCCESS(f"Updated profile for: {student_name}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
