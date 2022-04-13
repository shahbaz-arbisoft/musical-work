import csv

from django.core.management.base import BaseCommand, CommandError

from musicalapp.models import MusicalWork, Contributor


class Command(BaseCommand):
    help = 'Reconciled Work Data into Database'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='File path for csv file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['filepath']
        try:
            with open(file_path) as csv_file:
                csv_dict_reader = csv.DictReader(csv_file, delimiter=',')
                row_count = 0
                for row in csv_dict_reader:
                    is_contributor = True
                    contributors = [Contributor.objects.get_or_create(name=contributor.strip())[0] for contributor in
                                    row['contributors'].split('|')]
                    if row['iswc']:
                        musical, _ = MusicalWork.objects.get_or_create(title=row['title'], ISWC=row['iswc'])
                    else:
                        try:
                            musical = MusicalWork.objects.get(title=row['title'])
                            db_contributors = musical.contributors.values_list('name', flat=True)
                            file_contributors = [contributor.name for contributor in contributors]
                            is_contributor = bool(set(db_contributors) & set(file_contributors))
                        except MusicalWork.DoesNotExist:
                            continue
                    if is_contributor:
                        musical.contributors.add(*contributors)
                    row_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'{row_count} rows executed from this file'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File at this path "{file_path}" does not exist')
        except Exception as ex:
            print(ex)
