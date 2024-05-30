# mainpage/management/commands/load_courses.py

import csv
from django.core.management.base import BaseCommand
from mainpage.models import Course

class Command(BaseCommand):
    help = 'Load courses from CSV files'

    def handle(self, *args, **kwargs):
        platforms = ['edx', 'skillshare', 'coursera', 'udemy']
        for platform in platforms:
            file_path = f'/Users/pranav/Goal-Based-content-recommendation/BG1/mainpage/management/commands/edx.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Course.objects.create(
                        platform=platform,
                        title=row.get('title', ''),
                        description=row.get('description', ''),
                        instructor=row.get('instructor', ''),
                        rating=row.get('rating', 0),
                        duration=row.get('duration', ''),
                        level=row.get('level', ''),
                        link=row.get('link', ''),
                        skills=row.get('skills', ''),
                        students=row.get('students', 0) #.split(" ")[0].replace(",","")
                    )
        self.stdout.write(self.style.SUCCESS('Courses loaded successfully'))
