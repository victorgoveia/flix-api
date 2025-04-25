import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django_countries import countries
from actors.models import Actor


class Command(BaseCommand):
    help = 'Import actors from a CSV file with update and logging'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='CSV file name containing actor data'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        self.stdout.write(self.style.NOTICE(f'📂 Importing actors from file: {file_name}'))

        NAME_TO_CODE = {name: code for code, name in countries}

        created_count = 0
        updated_count = 0
        skipped_count = 0

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']

                try:
                    birth_date = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                except ValueError:
                    self.stdout.write(self.style.WARNING(f'❌ Invalid date format for: {name}: {row['birthday']}'))
                    skipped_count += 1
                    continue

                nationality_name = row['nationality']
                country_code = NAME_TO_CODE.get(nationality_name)

                if not country_code:
                    self.stdout.write(self.style.WARNING(f'❌ Unknown nationality: {nationality_name}. Skipping {name}'))
                    skipped_count += 1
                    continue

                actor, created = Actor.objects.update_or_create(
                    name=name,
                    birth_date=birth_date,
                    defaults={
                        'nationality': country_code,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'✅ Created new actor: {name}.'))
                    created_count += 1
                else:
                    self.stdout.write(self.style.NOTICE(f'✏️ Updated existing actor: {name}.'))
                    updated_count += 1

        self.stdout.write('\n')
        self.stdout.write(self.style.SUCCESS('✅ Import finished successfully.'))
        self.stdout.write(self.style.SUCCESS(f'✅ Created: {created_count}'))
        self.stdout.write(self.style.NOTICE(f'✏️ Updated: {updated_count}'))
        self.stdout.write(self.style.WARNING(f'⏭️ Skipped: {skipped_count}'))
