import csv

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from musicalapp.models import Work, Contributor


class Command(BaseCommand):
    help = 'Ingest Musical Work Data into Database tables'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='File path for csv file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['filepath']
        try:
            with open(file_path) as csv_file:
                csv_dict_reader = csv.DictReader(csv_file, delimiter=',')
                row_count = 0
                for row in csv_dict_reader:
                    try:
                        work_obj, _ = Work.objects.update_or_create(title=row['title'], defaults={'ISWC': row['iswc']})
                    except IntegrityError:
                        continue
                    contributors = [Contributor.objects.get_or_create(name=contributor.strip())[0] for contributor in
                                    row['contributors'].split('|')]
                    work_obj.contributors.add(*contributors)
                    row_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'{row_count} rows executed from this file'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File at this path "{file_path}" does not exist')
