import csv
from django.core.management.base import BaseCommand
from rbtcwebapp.models import Component  # Replace with your actual model

class Command(BaseCommand):
    help = 'Import components from CSV'

    def handle(self, *args, **kwargs):
        with open('E:/Projectss/robotics_website/rbtcwebsite/rbtcwebapp/management/commands/cleaned_lab_components.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            successful_imports = 0
            failed_imports = 0

            for row in reader:
                try:
                    Component.objects.create(
                        category=row[0],  # First column is category
                        name=row[1]       # Second column is component name
                    )
                    successful_imports += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Failed to import: {row} - {e}'))
                    failed_imports += 1

            self.stdout.write(self.style.SUCCESS(f'Successfully imported {successful_imports} components'))
            self.stdout.write(self.style.WARNING(f'Failed to import {failed_imports} components'))